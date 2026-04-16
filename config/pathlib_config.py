from pathlib import Path


def get_relative_path(relative_path: str):
        
    config_dir = Path(__file__).parent
            

    root_dir = config_dir.parent
                    
    return root_dir / relative_path


def get_scanner_log_path():
    return get_relative_path("log/scanner.log")
