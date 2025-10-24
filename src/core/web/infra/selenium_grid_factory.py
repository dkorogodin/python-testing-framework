from src.core.data.configs.configs_manager import ConfigsManager
from src.core.web.infra.selenium_grid_docker_compose import SeleniumGridDockerCompose
from src.core.web.infra.selenium_grid_service import SeleniumGridService
from src.core.web.infra.selenium_grid_test_container import SeleniumGridTestContainer
from src.core.web.infra.selenium_grid_type import SeleniumGridType


class SeleniumGridFactory:
    @staticmethod
    def get_selenium_grid_service(configs_manager: ConfigsManager) -> SeleniumGridService:
        service_type = SeleniumGridType.from_property(configs_manager.web_configs.selenium_grid)

        if service_type == SeleniumGridType.DOCKER_COMPOSE:
            return SeleniumGridDockerCompose(configs_manager.web_configs)
        else:
            return SeleniumGridTestContainer(configs_manager.web_configs)
