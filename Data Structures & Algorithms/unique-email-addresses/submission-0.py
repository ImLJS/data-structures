class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for char in emails:
            local, domain = char.split('@')
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)