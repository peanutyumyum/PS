import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class No10828 {

    public static void main(String[] args) throws IOException{
        solution();
    }

    public static void solution() throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Integer times = Integer.parseInt(br.readLine());

        // Stack은 배열로 구현한다. size는 stack의 size와 pointer의 역할을 수행한다.
        int[] stack = new int[times];
        int size = 0;

        for(int i = 0; i < times; i++) {

            String command = br.readLine();

            if (command.startsWith("push")) {
                
                int data = Integer.parseInt(command.substring(5).trim());
                stack[size] = data;
                size++;

            } else if (command.equals("pop")) {

                if (size < 1) {
                    bw.write(-1 + "\n");
                } else {
                    bw.write(stack[size - 1] + "\n");
                    stack[size - 1] = 0;
                    size--;
                }
                
            } else if (command.equals("size")) {

                bw.write(size + "\n");

            } else if (command.equals("empty")) {

                if (size < 1 ) {
                    bw.write(1 + "\n");
                } else {
                    bw.write(0 + "\n");
                }

            } else if (command.equals("top")) {

                if (size < 1) {
                    bw.write(-1 + "\n");
                } else {
                    bw.write(stack[size - 1] + "\n");
                }
                
            }
        }
        
        br.close();
        
        bw.flush();
        bw.close();
    }
}