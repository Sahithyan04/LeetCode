class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        int[] current = intervals[0];

        ArrayList<int[]> result = new ArrayList<>();

        for(int i = 1; i < intervals.length; i++){
            if(current[1] >= intervals[i][0]){
                current[1] = (current[1] > intervals[i][1])? current[1]:intervals[i][1];
            }else{
                result.add(current);
                current = intervals[i];
            }
        }

        result.add(current);
        return result.toArray(new int[result.size()][]);
       
    }
}