from src.core.data.configs.db_configs import DbConfigs
from src.core.db.infra.db_local import DbLocal
from src.core.db.infra.db_service import DbService
from src.core.db.infra.db_test_container import DbTestContainer
from src.core.db.infra.db_type import DbType


class DbFactory:
    @staticmethod
    def get_db_service(db_config: DbConfigs) -> DbService:

        service_type = DbType.from_property(db_config.db_infra)

        if service_type == DbType.LOCAL:
            return DbLocal(db_config)
        else:
            return DbTestContainer(db_config)
