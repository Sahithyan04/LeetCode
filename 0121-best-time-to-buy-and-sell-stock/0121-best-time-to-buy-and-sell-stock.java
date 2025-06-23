class Solution {
    public int maxProfit(int[] prices) {

        int min_price = Arrays.stream(prices).max().getAsInt();
        int max_price = Arrays.stream(prices).min().getAsInt();

        int max_profit = 0;
        for(int i =0 ; i < prices.length; i++){
            if (prices[i] < min_price) {
                min_price = prices[i];
                max_price =0;
            }if(prices[i]>max_price){
                max_price = prices[i];
                
            }
            int diff = max_price - min_price;
            max_profit = (max_profit > diff) ? max_profit:diff;

        }return max_profit;



        
    }
}