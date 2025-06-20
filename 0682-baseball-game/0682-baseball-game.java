class Solution {
    public int calPoints(String[] operations) {
        Stack <Integer> stk = new Stack<>();
        for (String strn : operations){
            if (strn.equals("C")){
                stk.pop();
            }else if (strn.equals("D")){
                int n = stk.peek();
                stk.push(n*2);
            }else if (strn.equals("+")){
                int a = stk.pop();
                int b = stk.peek();
                stk.push(a);
                stk.push(a+b);
            }else {
                stk.push(Integer.parseInt(strn));
            }


        }

        int sum = 0;
        for (int i:stk){
            sum += i;
            
        }return sum;
        
    }
}


