class SomeClass {
  public int a;
  public double b;
  public void dummy() {}
}
public class Test23 {
    public static void main(String[] args){
    }

    public SomeClass[] good() {
      return new SomeClass[0];
    }

    public SomeClass[] bad() {
      return null;
    }
}


