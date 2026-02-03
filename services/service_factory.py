from services.general.general_service import GeneralService
from services.auth.authentication_service import AuthenticatonService
from services.service import Service

class ServiceFactory:
    
    @staticmethod
    def create_service(service_type: str) -> Service:
        if service_type == "general":
            return GeneralService()
         
        elif service_type == "authentication":
            return AuthenticatonService()
        # Add more service types as needed
        raise ValueError(f"Unknown service type: {service_type}")