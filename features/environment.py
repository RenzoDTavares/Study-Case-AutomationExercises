import sys
import os
import datetime
import shutil 
from behave.model_core import Status

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from drivers.driver_manager import DriverManager
from utils.logger import get_logger

log = get_logger(__name__)

REPORT_DIR = "reports"
BASE_SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")

def before_all(context):
    if os.path.exists(REPORT_DIR):
        log.warning(f"Limpando o diretório de reports e evidências: {REPORT_DIR}")
        try:
            shutil.rmtree(REPORT_DIR)
        except OSError as e:
            log.error(f"Erro ao tentar remover diretório {REPORT_DIR}: {e}")
            
    if not os.path.exists(BASE_SCREENSHOT_DIR):
        os.makedirs(BASE_SCREENSHOT_DIR)
        log.info(f"Diretório de evidências base criado: {BASE_SCREENSHOT_DIR}")

def before_scenario(context, scenario):
    
    scenario_name_clean = "".join([c if c.isalnum() or c in [' ', '-', '_'] else "" for c in scenario.name])
    scenario_name_clean = scenario_name_clean.strip().replace(" ", "_")
    
    context.current_scenario_dir = os.path.join(BASE_SCREENSHOT_DIR, scenario_name_clean)
    
    if not os.path.exists(context.current_scenario_dir):
        os.makedirs(context.current_scenario_dir)
        log.info(f"Pasta de evidência criada: {context.current_scenario_dir}")

    try:
        context.driver = DriverManager.get_driver(browser='chrome')
        context.driver.maximize_window()
        log.info(f"--> Iniciando Cenário: {scenario.name}")
    except Exception as e:
        log.critical(f"Falha crítica ao inicializar driver: {e}")
        raise

def after_step(context, step):
    if hasattr(context, 'driver'):
        try:
            timestamp = datetime.datetime.now().strftime("%H-%M-%S")
            
            step_name_clean = "".join([c if c.isalnum() else "_" for c in step.name])[:40]
            status_label = step.status.name.upper()
            
            filename = f"{timestamp}_{status_label}_{step_name_clean}.png"
            
            target_dir = getattr(context, 'current_scenario_dir', BASE_SCREENSHOT_DIR)
            file_path = os.path.join(target_dir, filename)
            
            context.driver.save_screenshot(file_path)
            
            if hasattr(context, 'embed'):
                screenshot_bytes = context.driver.get_screenshot_as_png()
                context.embed(mime_type="image/png", data=screenshot_bytes, caption=f"{status_label}: {step.name}")
                
        except Exception as e:
            log.error(f"Erro ao salvar evidência: {e}")

def after_scenario(context, scenario):
    """Encerra o driver após cada cenário."""
    if hasattr(context, 'driver'):
        DriverManager.quit_driver(context.driver)
        log.info(f"<-- Finalizando Cenário: {scenario.name}")