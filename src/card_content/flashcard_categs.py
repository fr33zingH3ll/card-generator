from mechanics.element import Element


class FlashCardCategs:

    # 1.Créez un logo qui représente le monde des langages de programmation.
    # 2.Générez un logo simple et instructif pour représenter les concepts informatiques de base.
    # 3.Imaginez un logo qui symbolise la connectivité et le réseau informatique
    # 4.Concevez un logo qui évoque la sécurité informatique et la protection des données.
    # 5.Créez un logo qui incarne la gestion des bases de données et le stockage d'informations.
    # 6.Générez un logo qui représente le contrôle et la gestion des systèmes d'exploitation.
    # 7.Imaginez un logo pour le développement web, en mettant en avant le design et le contenu en ligne.
    # 8.Concevez un logo qui évoque l'intelligence artificielle et l'apprentissage automatique.
    # 9.Créez un logo qui représente le matériel informatique, y compris les composants matériels.
    # 10.Générez un logo pour le développement d'applications mobiles, en mettant en avant la mobilité et l'accessibilité.

    PROGRAMMING_LANGUAGES = Element("ProgrammingLanguages")
    BASIC_COMPUTER_CONCEPTS = Element("BasicComputerConcepts")
    COMPUTER_NETWORKS = Element("ComputerNetworks")
    COMPUTER_SECURITY = Element("ComputerSecurity")
    DATABASES = Element("Databases")
    OPERATING_SYSTEMS = Element("OperatingSystems")
    WEB_DEVELOPMENT = Element("WebDevelopment")
    ARTIFICIAL_INTELLIGENCE_AND_MACHINE_LEARNING = Element("ArtificialIntelligenceAndMachineLearning")
    COMPUTER_HARDWARE = Element("ComputerHardware")
    MOBILE_APP_DEVELOPMENT = Element("MobileAppDevelopment")

    ALL = [
        
        PROGRAMMING_LANGUAGES,
        BASIC_COMPUTER_CONCEPTS,
        COMPUTER_NETWORKS,
        COMPUTER_SECURITY,
        DATABASES,
        OPERATING_SYSTEMS,
        WEB_DEVELOPMENT,
        ARTIFICIAL_INTELLIGENCE_AND_MACHINE_LEARNING,
        COMPUTER_HARDWARE,
        MOBILE_APP_DEVELOPMENT
    ]
    _CATEGS_BY_NAME = {element.name.lower(): element for element in ALL}

    def get_categ_by_name(name: str) -> Element:
        return FlashCardCategs._CATEGS_BY_NAME[
            name.lower()]
