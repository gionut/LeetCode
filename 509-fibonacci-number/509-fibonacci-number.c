int fib(int n){
    if(n == 0) return 0;
    int prev = 1;
    int lastPrev = 0;
    for(int i = 1; i < n; i++) {
        prev = prev + lastPrev;
        lastPrev = prev - lastPrev;
    }
    return prev;
}