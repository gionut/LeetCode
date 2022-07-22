/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getPriorPivot(struct ListNode* head, int x){
    struct ListNode* priorPivot = NULL;
    
    struct ListNode* crt = head;
    while(crt != NULL) {
         if(priorPivot == NULL && crt->next != NULL && crt->next->val >= x) {
            priorPivot = crt;
        }
        crt = crt->next;
    }
    
    return priorPivot;
}

struct ListNode* removeNextAndReturn(struct ListNode* prior) {
    struct ListNode* aux;
    aux = prior->next;
    
    prior->next = prior->next->next;
        
    return aux;
}

void insertAfter(struct ListNode* node, struct ListNode* toInsert) {
    toInsert->next = node->next;
    node->next = toInsert;
}

int hasNext(struct ListNode* node) {
    if(node->next != NULL)
        return 1;
    return 0;
}

struct ListNode* partition(struct ListNode* head, int x){
    struct ListNode helperNode;
    helperNode.next = head;
    helperNode.val = 999;
    
    struct ListNode* priorPivot = getPriorPivot(&helperNode, x);
    if(priorPivot == NULL)
        return head;
    
    struct ListNode* crt = priorPivot;
    
    while(crt != NULL) {
       if(hasNext(crt) == 1 && crt->next->val < x) {
           struct ListNode* removed = removeNextAndReturn(crt);
           insertAfter(priorPivot, removed);
           priorPivot = removed;       
        }
        else
            crt = crt->next;    
    }
    
    
    return helperNode.next;
}