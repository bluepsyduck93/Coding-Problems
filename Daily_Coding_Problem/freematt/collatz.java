import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class collatz {

    public static ArrayList<ArrayList<Integer>> collatz(int n){
        ArrayList<ArrayList<Integer>> seqList = new ArrayList<ArrayList<Integer>>();
        int m = n;

        for(int i = 2; i <= m; i ++){
            int target = i;
            ArrayList<Integer> subArray = new ArrayList<Integer>();
            subArray.add(i);
            int count = 0;
            while (target > 1) {
                if (target % 2 == 0) {
                    target = target / 2;
                    subArray.add(target);
                    count++;
                } else if (target % 2 == 1) {
                    target = 3 * target + 1;
                    subArray.add(target);
                    count++;
                }
            }
            seqList.add(subArray);
        }
        System.out.println(seqList);
        return seqList;
    }

}
