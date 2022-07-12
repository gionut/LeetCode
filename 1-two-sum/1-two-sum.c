

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int integersAscending(const void* a, const void* b){
   return ( *(int*)a - *(int*)b );
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int sorted[numsSize];
    memcpy(sorted, nums, numsSize*sizeof(int));
    qsort(sorted, numsSize, sizeof(int), integersAscending);
    
    int small = 0;
    int big = numsSize-1;
    while(small < big){
        int sum = sorted[small] + sorted[big];
        
        if(sum == target) break;
        else if(sum > target) big--;
        else small++;
    }
    
    int i = 0;
    for(i; nums[i] != sorted[small]; i++);
    small = i;
    i = numsSize-1;
    for(i; nums[i] != sorted[big]; i--);
    big = i;

    *returnSize = 2;
    int* result = (int*) malloc(2*sizeof(int));
    result[0] = small;
    result[1] = big;
    return result;
}