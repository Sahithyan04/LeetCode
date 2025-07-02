class Solution {
    public String convert(String s, int numRows) {
        

        if (numRows == 1){
            return s;
        }
        boolean forward = true ;
        String res[] = new String[numRows];
        Arrays.fill(res, "");
        int k = 0;
        for(int i = 0 ; i  < s.length() ; i++) {
            if(k == 0 && forward == true  ) {
                res[k] += s.charAt(i);
                k ++;               
            }else if (k == 0 && !forward ){
                res[k] += s.charAt(i);
                k ++;
                forward = true;

            }else if(k == numRows-1 && forward){
                res[k] += s.charAt(i);
                forward = false;
                k--;
            }else if (forward){
                res[k] += s.charAt(i);
                k ++;            
            }else{
                res[k] += s.charAt(i);
                k--;
            }
        }//System.out.print(Arrays.toString(res)); 
        return String.join("",res);
    }
}