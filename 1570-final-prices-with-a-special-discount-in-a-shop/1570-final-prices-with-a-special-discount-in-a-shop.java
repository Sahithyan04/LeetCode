class Solution {
    public int[] finalPrices(int[] prices) {

        Stack <Integer> stack = new Stack<Integer>();
        Stack <Integer> index = new Stack<Integer>();
        int[] ans = new int[prices.length];

        for (int i=0;i<prices.length;i++){
            while (!stack.isEmpty() && prices[i] <= stack.peek()){
                ans[index.pop()] = stack.pop() - prices[i];          
            }
            index.push(i);  
            stack.push(prices[i]);
                      
        }
        while(!stack.isEmpty()){
            ans[index.pop()] = stack.pop();
        }
        return ans;
        
    }
}