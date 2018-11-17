class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # used for storing only the unique emails
        results = set()
        for email in emails:
            # separating out the local and domain names
            tokenized = email.split('@')
            local = tokenized[0]
            domain = tokenized[1]
            # getting rid of the dots because they don't matter
            local = local.replace(".", "")
            local_uniq = local
            if '+' in local:
                local_tokenized = local.split("+")
                # keeping only the part before the plus
                local_uniq = local_tokenized[0]
            # constructing unique email address
            uniq_email = local_uniq + "@" + domain
            results.add(uniq_email)
        return len(results)

sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))