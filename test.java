public class Test {
  int xxx;
    public static void main(String[] args){
    	if ("walmart" == "offer"){
    	    return;
    	}
    	if ("walmart" != "offer"){
    	    return;
    	}
    	String s = "A";
    	if (s == "offer"){
    	    return;
    	}
    }
}

class Empty {
  public int retInt() {return 1;}
  public Test retTest() {return Test();}
  public int[] retIntArr() {int[] a; return a;}
  public Test[] retTestArr() {return null;}
  public int[][] retInt2dArr() {}
}
