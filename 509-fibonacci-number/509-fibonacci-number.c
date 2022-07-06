int fib(int n){
    if(n == 0) return 0;
    int prev = 1;
    int lastPrev = 0;
    while(n > 1){
        prev = prev + lastPrev;
        lastPrev = prev - lastPrev;
        n--;
    }
    return prev;
}