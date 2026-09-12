from dataclasses import dataclass, field
from typing import Any

@dataclass
class ApiOperation:
    method: str
    path: str
    operation_id: str
    summary: str = ''

@dataclass
class ApiRegistry:
    operations: list[ApiOperation] = field(default_factory=list)

    def register_openapi(self, document: dict) -> list[ApiOperation]:
        for path, item in document.get('paths', {}).items():
            for method, operation in item.items():
                if method.lower() not in {'get','post','put','patch','delete','head','options'}:
                    continue
                self.operations.append(ApiOperation(method.upper(), path, operation.get('operationId', f'{method}_{path}'), operation.get('summary','')))
        return self.operations
