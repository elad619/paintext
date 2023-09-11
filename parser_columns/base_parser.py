from abc import ABCMeta, abstractmethod

class BaseParser(metaclass=ABCMeta):

    @abstractmethod
    def parse_document(self, document_content: str) -> str:
        raise NotImplementedError
