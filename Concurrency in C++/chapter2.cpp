#include<iostream>
#include<thread>

void do_something(int i){
    std::cout<<".";
}

void do_something_in_current_thread(){
    std::cout<<"doing something in current thread"<<std::endl;
}

struct func{
    int& i;
    func(int& i_):i(i_){}
    void operator() (){
        for(unsigned j=0;j<1e7; ++j){
            do_something(i);
        }
    }
};

void oops(){
    int some_local_state=0;
    func my_func(some_local_state);
    std::thread m_thread(my_func);
    m_thread.detach();
}

void f(){
    int some_local_state = 0;
    func my_func(some_local_state);
    std::thread t(my_func);
    try{
        do_something_in_current_thread();
        t.join();
        std::cout<<"f completed:"<<std::endl;
    }
    catch(...){
        t.join();
        std::cout<<"error"<<std::endl;
        throw;
    }
}

int main(){
    f();
    oops();
    return 0;
}