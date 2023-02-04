class Student{
    
    String name;
    int age;
    String email;

    public Student(String n, int a, String e) {
        this.name = n;
        this.age = a;
        this.email = e;
    }

    public String getName(){
        return name;
    }


}

class Program{
    public static void main(String[] args) {
        Student shpend = new Student("Shpend", 99, "shpendaliu@gmail.com");
        System.out.println(shpend);
        System.out.println(shpend.getName());
    }
}