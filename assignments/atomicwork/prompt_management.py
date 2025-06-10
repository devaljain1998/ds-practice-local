from collections import defaultdict
from sortedcontainers import SortedList
from typing import Optional, Tuple, Dict, List

class PromptManager:
    def __init__(self):
        # Structure: promptKey -> {(tenant_id, user_id): SortedList[(version, text)]}
        self.prompts: Dict[str, Dict[Tuple[Optional[str], Optional[str]], SortedList]] = defaultdict(dict)
    
    def _get_key(self, tenant_id: Optional[str], user_id: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
        return (tenant_id, user_id)
    
    def _get_or_create_list(self, prompt_key: str, tenant_id: Optional[str], user_id: Optional[str]) -> SortedList:
        key = self._get_key(tenant_id, user_id)
        if key not in self.prompts[prompt_key]:
            self.prompts[prompt_key][key] = SortedList()
        return self.prompts[prompt_key][key]

    def add_prompt(self, prompt_key: str, prompt_text: str, tenant_id: Optional[str] = None, 
                  user_id: Optional[str] = None) -> int:
        prompts = self._get_or_create_list(prompt_key, tenant_id, user_id)
        version = len(prompts) + 1 if prompts else 1
        prompts.add((version, prompt_text))
        return version

    def get_prompt(self, prompt_key: str, tenant_id: Optional[str] = None, 
                  user_id: Optional[str] = None) -> Tuple[int, str]:
        prompts = self._get_or_create_list(prompt_key, tenant_id, user_id)
        if not prompts:
            raise KeyError(f"No prompt found for key: {prompt_key}")
        return prompts[-1]

    def rollback_prompt(self, prompt_key: str, to_version: int, tenant_id: Optional[str] = None, 
                       user_id: Optional[str] = None) -> None:
        prompts = self._get_or_create_list(prompt_key, tenant_id, user_id)
        if not prompts:
            raise KeyError(f"No prompt found for key: {prompt_key}")
            
        idx = prompts.bisect_left((to_version, ""))
        if idx >= len(prompts) or prompts[idx][0] != to_version:
            raise ValueError(f"Version {to_version} not found")
        
        # Keep versions up to and including the target version
        key = self._get_key(tenant_id, user_id)
        self.prompts[prompt_key][key] = SortedList(prompts[:idx + 1])

    def get_prompt_history(self, prompt_key: str, tenant_id: Optional[str] = None, 
                          user_id: Optional[str] = None) -> List[Tuple[int, str]]:
        prompts = self._get_or_create_list(prompt_key, tenant_id, user_id)
        return list(prompts)




