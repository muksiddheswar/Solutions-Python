#include <vector>
#include <iostream>
using namespace std;

class Person
{
    protected:
        string name;
        int age; 
    
    public:
        virtual void getdata() {
            cin >> this->name >> this->age;
        }
        virtual void putdata() {
            cout << this->name << " " << this->age << endl;
        }
};

class Professor : public Person{
    private:
        int publications;
        int cur_id;
    public:
        static int id;
        Professor(){
            cur_id = ++id;
        }

        void getdata(){
            cin>>name>>age>>publications;
        }

        void putdata(){
            cout<<name<<" "<<age<<" "<<publications<<" "<<cur_id<<endl;
        }
};

class Student : public Person{
    private:
        int marks[6];
        int cur_id;
    public:
        static int id;
        Student(){
            cur_id = ++id;
        }

        void getdata(){
            int i;
            cin>>name>>age;
            for(i=0; i<6; i++)
                cin>>marks[i];
        }

        void putdata(){
            int s =0, i;
            for(i=0; i<6; i++)
                s += marks[i];

            cout<<name<<" "<<age<<" "<<s<<" "<<cur_id<<endl;
        }
};

int Professor::id = 0;
int Student::id = 0;


int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
