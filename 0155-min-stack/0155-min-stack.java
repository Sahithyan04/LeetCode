class MinStack {

    Stack <Integer> stack;
    Stack <Integer> MinStack;

    public MinStack() {
        this.MinStack = new Stack<Integer>();
        this.stack = new Stack<Integer>();
        
    }
    
    public void push(int val) {

        stack.push(val);
        if (MinStack.isEmpty() || MinStack.peek() >= val) {
            MinStack.push(val);
            
        }else{
            MinStack.push(MinStack.peek());
        }
        
    }
    
    public void pop() {
        stack.pop();
        MinStack.pop();
    }
    
    public int top() {
        return stack.peek();
        
    }
    
    public int getMin() {
        return MinStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */