"""
 Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number
 of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and 
the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

A binary search tree has elements on the left > node > right

Hint: 
Draw an edge between emails in the same account

# Rephrase:Given a list of accounts retrn a list with emails merged

Output: List of List of strings, in anyorder. Each inner list starts with an email and then an ordered list of emails

Data structure: 
Treating like a graph,so will do DFS and use a stack
List to track pointers to all connected nodes

Steps: 
Start with an email in the [0,0] position of all emails.
Traverse to the [1,0] position - the start of the next list of emails. Iterate through all emails until finding the same email as the first 
Once found, update the first entry with a pointer towards this position for the next email and the entry for this inner list with a pointer back to the first list
Once a connection has been established, do not need to check links between these two lists in particular
After repeating for all nodes, iterate through the list of pointers, merging each list then finally sorting each

"""

from typing import Optional, List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        pointers = [[]]*len(accounts)
        compared = set()

        s = [accounts[0][1:]]
        # BFS
        idx=0
        while s:
            email_list =s.pop()
            if idx < len(accounts)-1:
                for email in email_list:
                    for j in range(idx+1, len(accounts)):
                        if j not in pointers[idx] \
                            and j not in compared:
                            if email in accounts[j]:
                                pointers[idx].append(j)
                                pointers[j].append(idx)
                                break 
                    
                compared.add(idx)
            
            idx+=1
            if idx < len(accounts):
                s.append(accounts[idx][1:])

        ret_list = []
        added = set()
        for i, pointers_list in enumerate(pointers):
            if i not in added:
                name = accounts[i]
                cur_list = accounts[i]
                for p in pointers_list:
                    cur_list += accounts[p][1:]
                    added.add(p)
                
                cur_list.sort()
                ret_list.append([name]+cur_list)

        return ret_list

# Produces many copies of emails and mergedlists
        

"""
Leetcode Solution

1. Create an adjacency list. For each account, add an edge between the first email and each other email in the same account
2. Traverse over account. For each account, check if first email in account was already visited. If so, do not start a new DFS
3. During the DFS stored traversed emails in array mergedAccount
4. After DFS 

The meat is in checking the adjacency list (hash map). In the nth iteration, an email that's already in the adjacency list will be found and have all its current neighbors
added to the list

"""

class Solution:
    def __init__(self):
        self.visited=set()
        self.adjacent = {}

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        for account in accounts:
            inner_a = len(account)
            # Build adjacency list
            first_email = account[1]
            for j in range(2,inner_a):
                email=account[j]

                if first_email not in self.adjacent:
                    self.adjacent[first_email] = []
                
                self.adjacent[first_email].append(email)
                if email not in self.adjacent:
                    self.adjacent[email] = []
                self.adjacent[email].append(first_email)

        # Traverse adjacency list    
        merged_accounts = []
        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in self.visited:
                merged_account = self.DFS([], first_email)
                merged_account.sort()
                if len(merged_account) >0:
                    merged_accounts.append([name]+merged_account)

        return merged_accounts

    def DFS(self,merged_account:List[str], email:str):
        self.visited.add(email)
        merged_account.append(email)

        if email not in self.adjacent:
            return merged_account

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                merged_account = self.DFS(merged_account, neighbor)

        return merged_account
                


"""
Leetcode Solution 2 - Disjoint Set Union

AKA "Union Find"
"""


            
