# 上机准备

## C++知识
### 数据类型及范围
- int 正负21亿(大约)
- long long 正负9*10^18(大约)
- float 提供7~8位有效数字
- double 提供15~16位有效数字 正负1.7*10^308次方(大约), 用double硬编码一个308位的数字在代码中可能通不过编译

| 类型 | 范围(十进制) | 内存大小 |
|--|--|--|
|char|-128~127|1 Byte|
|short|-32768~32767|2 Byte|
|unsigned short|0~65535|2 Byte|
|int/long|-2147483648~2147483647|4 Byte|
|unsigned int|0~4294967295|4 Byte|
|long long|-9223372036854775808~9223372036854775807 |8 Byte|
|float|-3.4E-38~3.4E+38|4 Byte|
|double|1.7E-308~1.7E+308|8 Byte|

```c++
numeric_limits<long long>::min()    // 获取long long的最小值
numeric_limits<long long>::max()
```


### 各个类型使用c语言时的输入
(1) 输入long long时。 %lld"和"%llu"是linux下gcc/g++用于long long int类型(64 bits)输入输出的格式符，而"%I64d"和"%I64u"则是Microsoft VC++库里用于输入输出__int64类型的格式说明
(2) 输入float时。%f
(3) 输入double时。%lf   输出时用%f

### 科学表示法
- 10^9表示为`1e9`，而不是`10e9`

### 一些常用的判断函数
```c++
isalpha()  // 判断是否为英文字母
isalnum()  // 判断是否为英文字母或数字
islower()  // 判断是否为小写字母
isupper()  // 判断是否为大写字母
```

### 输出指定位数的小数
```c++
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double val = 0.12345;
    // 输出两位小数
    cout<< fixed << setprecision(2) << val << endl;

    // 不要用val * 100 再除100这种操作，会四舍五入？
    return 0;
}
```

### math
```c++
#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double PI = acos(double(-1));  // PI的值
    double e = exp(double(1)); // e的值
    cout<<log10(100)<<endl; // log10(100)输出2
    return 0;
}
```


### 随机数
```c++
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    srand((int)time(NULL));
    for(int i=0; i<1000; ++i){
        cout<<rand()<<endl;
    }
}

```

### 进制转换
```c++
#include <iostream>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <assert.h>

using namespace std;

string int2nradix(long long x, long long n){
    int digit;
    char ch;
    string res;
    do{
        digit = x%n;
        ch = digit>=10?('a'+(digit-10)):('0'+digit);
        res = ch + res;
        x /= n;
    }while(x);
    return res;
}

long long nradix2int(string &seq, long long n){
    long long res = 0;
    for(int i=0; i<seq.size(); ++i){
        if(isalpha(seq[i])){
            res = res*n + (tolower(seq[i]) - 'a') + 10;
        }
        else{
            res = res*n + (seq[i] - '0');
        }
    }
    return res;
}

void test1(){
    bool flag = false;
    srand((int)time(NULL));
    for(int i=0; i<100000; ++i){
        int n = abs(rand())%36;
        n = (n==0||n==1)?2:n;
        string seq = int2nradix(i, n);
        if(i != nradix2int(seq, n)){
            cout<<"error: "<<i<<" "<<seq<<" "<<nradix2int(seq, n)<<", 进制为: "<<n<<endl;
            flag = true;
        }
        else{
            // cout<<i<<"的"<<n<<"进制为"<<seq<<endl;
        }
    }
    if(!flag){
        cout<<"全部正确"<<endl;
    }
}

void test2(){
    srand((int)time(NULL));
    char buf[1024];
    for(int i=0; i<100000; ++i){
        int n = rand() % 36;
        n = (n==0||n==1)?2:n;
        memset(buf, 0, sizeof(buf));
        string s1 = int2nradix(i, n);
        itoa(i, buf, n);
        string s2(buf);
        assert(s1==s2);
        long long x = nradix2int(s2, n);
        assert(x==i);
    }
}

int main(){
    // c语言中输出
    printf("%o\n", 16);  // 8进制, 输出20
    printf("%d\n", 16);  // 10进制, 输出16
    printf("%x\n", 16);  // 16进制, 输出10

    // atoi()  c语言函数, 将10进制数字符串转换为10进制数
    // int atoi(const char *str)
    char s1[] = "12344321";
    cout<<atoi(s1)<<endl;

    // strtol() c函数 将一个任意进制的字符串转换为10进制数(int型)
    // endptr指向非法字符所在的位置
    // long int strtol(const char *nptr, char **endptr, int base)
    char *ptr;
    cout<<strtol(s1, &ptr, 5)<<endl;
    cout<<ptr<<endl;       // 无内容
    cout<<strtol(s1, &ptr, 4)<<endl;
    cout<<ptr<<endl;       // 因为进制为4, 所以原字符串中4为非法, 此处输出44321

    // itoa() c函数, 不是标准库函数. 受字母表限制, 只能转换2~36进制(10个阿拉伯字母+26个英文字母)
    // char*itoa(int value,char*string,int radix);
    char s2[10];
    itoa(16, s2, 16);     // 将16转换为16进制
    cout<<s2<<endl;       // 输出10
    itoa(71, s2, 36);     // 将71转换成36进制
    cout<<s2<<endl;       //输出1z


    // sprintf() c函数, 字符串格式化函数, 可以将10进制转换为8进制, 16进制
    // int sprintf(char *string, char *format [,argument,...]);
    // %[flags][width][.precision][length]specifier
    sprintf(s2, "%d", 12344321);    // 将12344321写入s2中
    cout<<s2<<endl;
    sprintf(s2, "I eat %d apples.", 1234);
    cout<<s2<<endl;           // 输出I eat 1234 apples.
    sprintf(s2, "%.2f", (double)123);
    cout<<s2<<endl;           // 输出123.00
    sprintf(s2, "%x", 15);
    cout<<s2<<endl;           // 输出f
    sprintf(s2, "%X", 15);
    cout<<s2<<endl;           // 输出F


    // c++ 按指定格式输出 (注意这样使用后, 需要清除这些标志位, 如在代码的60行必须重置回来)
    cout<<oct<<16<<endl;         // 把16按8进制输出, 即20
    cout<<dec<<16<<endl;         // 把16按10进制输出, 即16
    cout<<hex<<16<<endl;         // 把16按16进制输出, 即20
    cout<<bitset<8>(16)<<endl;  // 用长为8bitset将16按2进制输出, 即00010000

    // stoi() c++函数, 将所给的base进制的字符串str转换为10进制
    // idx指示的是第一个不合法字符所在的位置
    // int stoi (const string&  str, size_t* idx = 0, int base = 10);
    string st = "20 dddd";
    size_t sz;
    cout<<dec<<stoi(st, &sz, 10)<<endl;
    cout<<"不合法字段为: "<<st.substr(sz)<<endl;
    st = "20";
    cout<<stoi(st, nullptr, 8)<<endl;  // 将8进制串20转换为10进制, 即输出16

    // 利用stoi()函数可以实现任意进制到十进制的转换
    // 利用bitset可以实现10进制到2进制的转换
    // 利用itoa()实现从10进制到任意进制的转换
    // 需要自己实现从10进制到任意进制的转换

    test1();  // 测试自己写的函数
    test2();

    return 0;
}
```


### 运算符重载
```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Point{
    int x, y;
    Point(){}
    Point(int x, int y):x(x), y(y){}

    bool operator<(const Point &rhs)const{
        if(x < rhs.x) return true;
        else if(x == rhs.x) return y < rhs.y;
        else return false;
    }

    bool operator==(const Point &rhs)const{
        return x==rhs.x && x==rhs.y;
    }

    friend istream &operator>>(istream &ist, Point &po){
        return ist>>po.x>>po.y;
    }

    friend ostream &operator<<(ostream &ost, const Point &po){
        return ost<<"("<<po.x<<", "<<po.y<<")";
    }
};

template <typename T> void print(vector<T> &v){
    // for(typename vector<T>::iterator it=v.begin(); it!=v.end(); ++it){
    //     cout<<*it<<endl;
    // }
    for(auto it=v.begin(); it!=v.end(); ++it){
        cout<<*it<<endl;
    }
}

int main(){
    int n;
    Point tp;
    vector<Point> v;
    cin>>n;
    while(n--){
        cin>>tp;
        v.push_back(tp);
    }
    print(v);

    return 0;
}
```

### 文件读取
```c++
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int count_space(string &s){
    int cnt = 0;
    for(size_t i=0; i<s.size(); ++i){
        if(s[i] == ' '){
            ++cnt;
        }
    }
    return cnt;
}

int count_letter(string &s){
    int cnt = 0;
    for(size_t i=0; i<s.size(); ++i){
        if(isalpha(s[i])) ++cnt;
    }
    return cnt;
}

int main(){
    int x, y, cost;
    ifstream inp;
    ofstream oup;

    inp.open("input.txt");  // input.txt 每行格式为: x y cost
    oup.open("output.txt"); // 输出x+y+cost到output.txt, 一个一行

    while(inp>>x>>y>>cost){
        cout<<x<<" "<<y<<" "<<cost<<endl;
        oup<<x+y+cost<<endl;
    }
    inp.close();
    oup.close();

    string s;
    inp.open("input2.txt");
    /*
    input2.txt内容为一行行的英文句子, 如下:
    I am a student.
    you are a boy, she is a girl.
    */
    // getline() 读一行(遇到换行符结束当前行读入), cin>>遇到空格则结束一次读取(从标准流中读取时)
    int line_cnt = 0;
    while(getline(inp, s)){
        int spaces = count_space(s);
        int letters = count_letter(s);
        int symbols = s.size() - letters - spaces;
        cout<<"line("<<++line_cnt<<"): "<<s<<" 有"<<spaces<<"个空格, "<<letters<<" 个英文字母, "<<symbols<<"个标点符号"<<endl;
    }
    inp.close();

    stringstream sstr;
    inp.open("input3.txt");
    /*
    input3.txt内容为一行行的数据，每一行含有2个浮点数，用空行隔开，如下:
    1.23 4.56
    7.89 0.10
    */
    while(getline(inp, s)){
        double d1, d2;
        sstr<<s;       // 用s实例化stringstream, 也可以stringstream sstr(s);
        sstr>>d1>>d2;
        cout<<d1<<" "<<d2<<endl;
    }

    //  seekg() seekp()

    /* c语言版
    重定向 重定向后cin从input4.txt读入, 输出到output.txt
    freopen("input4.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    fclose(stdin);
    fclose(stdout);
    */
    return 0;
}

```
---
### STL

### STL各个容器的底层实现
- 来源[点击链接](https://www.cnblogs.com/westlife-11358/p/9427374.html)

| 容器 | 底层 | 特点 |
| -- | -- | -- |
| vector | 数组 | gcc以两倍进行扩容,支持快速随机访问 |
| list | 双向链表 | 不支持随机访问, 支持快速增删|
| deque | 中央控制器和多个缓冲区 | 支持首尾(中间不能)快速增删, 也支持随机访问|
| set | 红黑树 | 有序, 不重复|
| multiset | 红黑树 | 有序, 重复 |
| map | 红黑树 | 有序, 不重复 |


| 适配器 | 底层 | 特点 |
| -- | -- | -- |
| stack | list或deque |  FILO |
| queue | list或deque | FIFO |

### pair
```c++
#include <iostream>
#include <utility>

using namespace std;

int main(){
    pair<int, int> p1(1, 2);
    cout<<p1.first<<" "<<p1.second<<endl;

    // make_pair()
    return 0;
}
```

### string
```c++
#include <string>
#include <iostream>

using namespace std;

int main(){
    return 0;
}
```

### vector
```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

bool cmp(int &lhs, int &rhs){
    return lhs > rhs;
}

void print(vector<int> &v){
    for(size_t i=0; i<v.size(); ++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int main(){
    vector<int> v;

    /* 插入 */
    v.push_back(1);
    v.push_back(2);
    v.push_back(4);
    v.push_back(3);
    v.push_back(0);

    /* 遍历方式1 */
    cout<<"遍历方式1: ";
    for(size_t i=0; i<v.size(); ++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;

    /* 遍历方式2, 从头到尾 */
    cout<<"遍历方式2, 从头到尾: ";
    for(vector<int>::iterator it=v.begin(); it!=v.end(); ++it){
        cout<<*it<<" ";
    }
    cout<<endl;

    /* 遍历方式3, 从尾到头 */
    cout<<"遍历方式3, 从尾到头: ";
    for(vector<int>::reverse_iterator it=v.rbegin(); it!=v.rend(); ++it){
        cout<<*it<<" ";
    }
    cout<<endl;

    /* 从小到大排序 */
    sort(v.begin(), v.end());
    cout<<"从小到大排序: ";
    print(v);

    /* 从大到小排序 */
    sort(v.begin(), v.end(), cmp);
    cout<<"从大到小排序: ";
    print(v);

    /* 或者使用greater, 在头文件<functional>中 */
    v.push_back(7);
    sort(v.begin(), v.end(), greater<int>());
    cout<<"插入7后使用greater从大到小排序: ";
    print(v);

    /* 从数组的第i位起开始排序 */
    sort(v.begin()+2, v.end());
    cout<<"从数组的第i=2位起从小到大排序: ";
    print(v);


    cout<<v.size()<<endl;  // vector中数据项的个数

    cout<<v.max_size()<<endl; //vector中最多能放多少个数据项

    cout<<v.capacity()<<endl; // 当前vector开辟的空间能放多少数据项

    cout<<v.empty()<<endl; // bool型，返回vector是否为空

     v.reserve(100); // 将vector的capacity直接改为100, 即直接开辟100单位的长度，而不是每次不够后乘以2

    v.pop_back(); // 删除vector最后一个元素（只是移动指针，最后那个位置的元素仍然存储在那个位置）

    // assign()
    vector<int> tv;
    tv.push_back(1);
    tv.push_back(-1);
    print(tv);  // 输出1, -1
    tv.assign(7, 100);
    print(tv);  // 输出7个100, 之前的内存被抛弃，重新分配后并赋值7个100
    vector<int> tv2;
    tv2.push_back(7);
    tv2.push_back(8);
    tv.assign(tv2.begin(), tv2.end());
    print(tv);


    v.insert(v.begin()+2, 23, 2);  // 在下标2处插入23个2
    vector<int> another_vec(6, 3333);  // 构造一个含有6个3333的vector
    v.insert(v.begin(), another_vec.begin()+3, another_vec.end()); // 将another_vec从下标3开始到最后插入v中
    print(v);
    int arr[] = {1, 2, 3, 4, 5, 6};
    v.insert(v.begin(), arr, arr+6);
    print(v);

    v.erase(v.begin()+5);  // 删除下标为5的元素，即第六个元素
    print(v);
    v.erase(v.begin(), v.begin()+3); // 删除前3个元素，即左闭右开
    print(v);

    // 与another_vec交换内容，之前的迭代器、引用、指针仍然有效
    v.swap(another_vec);

    // 清空vector，使得size为0，但不保证重新分配空间。
    // 可以理解为只是修改了指针，但是原来的空间里仍然存储着之前的数据
    v.clear();

    // 若想把内存释放掉则如下操作，新构造一个vector交换给v。
    vector<int>().swap(v);

    return 0;
}
```
### list
```c++
#include <iostream>
#include <algorithm>
#include <list>
#include <vector>

using namespace std;

template<typename T>
void print(list<T> &L){
    for(typename list<T>::iterator it=L.begin(); it!=L.end(); ++it){
        cout<<*it<<" ";
    }
    cout<<endl;
}

bool cmp(int lva, int rva){
    return lva > rva;
}

int main(){
    list<int> L;

    // list底层是双向链表
    // list也有反向迭代器 list<int>::reverse_iterator
    // list迭代器不支持 L.begin()+1 运算, 但支持list<int>::iterator it = L.begin(); ++it;

    // 以下同vector一致
    L.empty();
    L.size();
    L.max_size();

    L.front(); // 获取第一个元素
    L.back(); // 获取最后一个元素

    L.push_back(1); // 插入末尾
    print(L);
    L.push_front(2); // 插入头
    print(L);
    L.pop_back();  // 删除最后一个元素
    print(L);
    L.pop_front(); // 删除第一个元素
    print(L);

    // insert()和vector一致
    L.insert(L.begin(), 2, 2333); // 在开头位置插入2个2333
    print(L);

    list<int>::iterator it = L.begin();
    ++it;
    L.insert(it, 3, 97); // 在下标1处插入3个97
    print(L);

    vector<int> v(3, 100);
    L.insert(L.begin(), v.begin(), v.end());  // 将vector指定范围的元素插入list中
    print(L);

    // erase()的定义
    // iterator erase (const_iterator position);
    // iterator erase (const_iterator first, const_iterator last);
    // 返回被删除元素的后一个位置
    it = L.begin();
    it = L.erase(it); // 删除第一个元素，将返回值赋给it，即it指向原来第二个元素(现在第一个)
    print(L);

    // advance(iterator &it, cnt) 令迭代器前进cnt个元素
    list<int>::iterator pt = L.begin();
    advance(pt, 5);

    // distance(iterator &frm, iterator &to) // 返回两个迭代器之间的距离
    distance(it, pt);

    L.erase(it, pt);  // 删除迭代器it和pt之间的元素(左闭右开)
    print(L);


    // sort() 复杂的nlogn, 可传入cmp
    L.sort(cmp);  // 从大到小排序
    print(L);


    // merge()
    list<double> first, second;
    first.push_back (3.1);
    first.push_back (2.2);
    first.push_back (2.9);
    second.push_back (3.7);
    second.push_back (7.1);
    second.push_back (1.4);
    first.sort();
    second.sort();
    first.merge(second);
    // merge后second为空
    cout<<second.size()<<endl;
    print(first);


    // remove(val) 删除list中值为val的项
    L.remove(97);


    // resize()
    // void resize (size_type n);
    // void resize (size_type n, const value_type& val);
    second.resize(10);        // resize为10个0
    second.resize(12, 2.33);  // 在之前的基础上插入两个2.33
    print(second);

    // reverse() 逆置链表
    second.reverse();
    print(second);

    // splice() splice是将那些元素转接到其他链表去
    // void splice (const_iterator position, list& x);  将x这整个list插入到position-1和position之间
    // void splice (const_iterator position, list& x, const_iterator i); 将链表x迭代器i所指向的元素插入到下标为position处
    // void splice (const_iterator position, list& x, const_iterator first, const_iterator last); 将链表x两个迭代器指示范围内(左闭右开)的元素插入到position-1和position之间

    // swap() 和vector一致

    // unique() 等价于algorithm中的unique

    return 0;
}
```

### queue
```c++
#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>

using namespace std;

struct Node{
    int frm, to;
    Node(){}
    Node(int frm, int to):frm(frm), to(to){}
};

int main(){
    queue<int> q;
    q.push(1);               // 插入队尾
    q.push(-1);

    cout<< q.back() <<endl;  // 获取队列最后一个元素, 即-1
    cout<< q.front() <<endl; // 获取队列第一个元素, 即1
    cout<< q.size() <<endl;  // 获取队列中元素个数, 即2

    q.pop();                 // 删除队头元素, 即1


    // 遍历队列方式
    while(!q.empty()){
        int fr = q.front();
        q.pop();;
        cout<<fr<<" ";
    }
    cout<<endl;

    // emplace()  c++11特性, 传入参数, 自动构造元素, 效率比传递拷贝要高些

    queue<Node> nq;
    nq.emplace(1, 2);
    nq.emplace(3, 4);
    while(!nq.empty()){
        cout<<nq.front().frm<<" "<<nq.front().to<<endl;
        nq.pop();
    }

    // swap()与其他容器大致相同

    return 0;
}

```

### deque
```c++
#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

int main(){

    deque<int> deq;

    // 支持的迭代器有
    // begin(), end(), rbegin(), rend()
    // cbegin(), cend(), crbegin(), crend()

    // size()  返回队列中当前元素个数
    // max_size() 返回队列最大能容纳元素的个数
    // empty() 队列为空时返回true

    // resize() 和之前的容器一致
    // void resize (size_type n); 当n小于现在队列的size()时，直接丢弃末尾
    // void resize (size_type n, const value_type& val); 当n大于现在队列的size()时，在末尾填充val

    // 支持操作符[]运算, 即可以随机存取
    // front() 获取第一个元素
    // back() 获取最后一个元素

    // push_back() 在队列末尾插入
    // push_front() 在第一个元素之前插入
    // pop_front() 删除队列第一个元素
    // pop_back() 删除最后一个元素
    // emplace_front() 根据参数构造队列元素并插入到队列第一个元素之前
    // emplace_back() 根据参数构造队列元素并插入到队列最后一个元素后

    // asign() 表现类似
    // insert() 表现类似
    // erase() 表现类似
    // swap() 表现类似
    // clear() 表现类似
    return 0;
}
```
### priority queue
```c++
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

struct Node{
    int frm, to, cost;
    Node(int frm, int to, int cost):frm(frm), to(to), cost(cost){}
    bool operator<(const Node &rhs)const{
        return cost < rhs.cost;
    }

    friend ostream &operator<<(ostream &os, const Node &n){
        return os<<n.frm<<" "<<n.to<<" "<<n.cost;
    }
};

template<typename T> void print(priority_queue<T> &pq){
    while(!pq.empty()){
        cout<<pq.top()<<" ";
        pq.pop();
    }
    cout<<endl;
}

void print(priority_queue<int, vector<int>, greater<int> > &pq){
    while(!pq.empty()){
        cout<<pq.top()<<" ";
        pq.pop();
    }
    cout<<endl;
}

int main(){
    // 默认是最大堆
    priority_queue<int> pq;
    pq.push(1);
    pq.push(-1);
    pq.push(-2);
    pq.push(2);
    print(pq);

    // 构建一个最小堆(注意传入的是greater)
    priority_queue<int, vector<int>, greater<int> > pq2;
    pq2.push(6);
    pq2.push(5);
    pq2.push(2);
    print(pq2);

    // empty() 类似
    // size() 类似
    // top() 取堆顶元素
    // push() 插入一个元素到堆中
    // emplace() 类似
    // pop()
    // swap()  行为类似

    // Node重载了<  即大顶堆要重载小于号，小顶堆要重载大于号
    priority_queue<Node> mq;
    mq.emplace(1, 2, 1);
    mq.emplace(5, 3, 100);
    mq.emplace(2, 23, 23);
    print(mq);

    // 若要实现一个小顶堆, 则要重载小于号, 我这里没有重载, 且队列实例化如下:
    /*
    bool operator>(const Node &rhs)const{
        return cost > rhs.cost;
    }

    priority_queue<Node, vector<Node>, greater<Node> > pq;
    */
    return 0;
}
```
### set
```c++
#include <iostream>
#include <utility>
#include <set>

using namespace std;

void print(set<int> &s){
    for(set<int>::iterator it=s.begin(); it!=s.end(); ++it){
        cout<<*it<<" ";
    }
    cout<<endl;
}

int main(){
    set<int> s;

    // 支持的迭代器有:
    // begin(), end(), rbegin(), rend()
    // cbegin(), cend(), crbegin(), crend()

    // empty() 类似
    // size() 类似
    // max_size() 类似

    // insert(), 返回一个pair<set<typename>::iterator, bool>
    pair<set<int>::iterator, bool> pa;
    s.insert(1);
    s.insert(2);
    pa = s.insert(5);
    cout<< *pa.first <<" "<<pa.second<<endl;
    pa = s.insert(5);  // 插入一个已经存在的元素，则返回的pair中的布尔值为false
    cout<< *pa.first <<" "<<pa.second<<endl;

    // insert() 和之前的容器一致，可以传入同一个容器的两个迭代器，将指示范围内的值插入
    int arr[] = {1, 2, 3, 4, 5};
    s.insert(arr, arr+5);   // 这种情况下无返回值
    // iterator insert (const_iterator position, const value_type& val); 这个没看懂返回值是个啥，反正目前用不着


    //erase() 左闭右开
    // iterator erase(const_iterator position);  删除迭代器指定位置的元素, 返回被删除的值得后一个元素的迭代器.(没有后继元素则返回end())
    // size_type erase(const value_type& val); 删除集合中值为val的元素，返回删除的个数(只可能是0个和1个？)
    // iterator erase (const_iterator first, const_iterator last); 删除两个迭代器指定范围内的元素, 返回被删除的最后一个元素的后一个元素的迭代器


    // swap() 类似
    // clear() 释放内存
    // emplace() 类似

    // find() 找到val, 则返回其迭代器，找不到则返回set::end
    // const_iterator find (const value_type& val) const;
    // iterator find (const value_type& val);
    set<int>::iterator it;
    it = s.find(1);
    if(it != s.end()){
        cout<<"yes"<<endl;
    }
    it = s.find(2333);
    if(it == s.end()){
        cout<<"no"<<endl;
    }

    // count() 查找值为val的元素的个数，结果为0或者1
    // size_type count(const value_type& val) const;
    cout<<s.count(5)<<endl;


    // lower_bound() 返回最左边值为val的元素的迭代器，不存在则返回set::end
    // upper_bound() 返回值为val的元素的后一个元素的迭代器, 不存在则返回set::end

    set<int> ns;
    for(int i=1; i<=7; ++i){
        ns.insert(i*10);
    }
    set<int>::iterator st = ns.lower_bound(20); //指向元素2
    set<int>::iterator ed = ns.upper_bound(60); //指向元素7
    ns.erase(st, ed);  // 删除20到60, 即ns中只有10, 70
    print(ns);

    // equal_range() 没看懂这个函数有什么意义
    return 0;
}
```
### multiset
```c++
#include <iostream>
#include <set>

using namespace std;

void print(multiset<int> &ms){
    for(multiset<int>::iterator it=ms.begin(); it!=ms.end(); ++it){
        cout<<*it<<" ";
    }
    cout<<endl;
}

int main(){
    multiset<int> ms;
    // multiset这玩意的存在感太低了

    // 支持的迭代器有:
    // begin(), end(), rbegin(), rend()
    // cbegin(), cend(), crbegin(), crend()

    // empty() 类似
    // size() 类似
    // max_size() 类似

    // insert()
    // iterator insert(const_iterator position, const value_type& val); 没看懂官网的那段代码
    // iterator insert(const value_type& val); 返回插入的值的迭代器
    // void insert(InputIterator first, InputIterator last);
    ms.insert(1);
    ms.insert(3);
    ms.insert(3);
    ms.insert(3);
    ms.insert(4);
    print(ms);

    // erase()
    //iterator  erase(const_iterator position); 返回被删除元素的后继元素的迭代器或为set::end
    // size_type erase(const value_type& val); 返回删除的个数
    // iterator  erase(const_iterator first, const_iterator last); 返回被删除元素的后继元素的迭代器或为set::end

    // swap() 类似
    // clear() 释放内存
    // emplace() 类似

    // find() 返回val的迭代器(最左边的那个元素)或者找不到返回multiset::end
    // const_iterator find(const value_type& val) const;
    // iterator find (const value_type& val);
    set<int>::iterator ptr = ms.find(3);
    cout<<*(--ptr)<<endl;  // 输出1

    // count() 返回值为val的元素的个数
    // size_type count(const value_type& val) const;

    // lower_bound() 返回值为val的，最左边的元素的迭代器，不存在返回multiset::end
    // upper_bound() 返回值为val的，最右边元素的后一个元素的迭代器，不存在则返回multiset::end

    // equal_range() 返回值为val的元素的范围，用两个迭代器指示，放在一个pair中
    // pair<const_iterator,const_iterator> equal_range(const value_type& val) const;
    // pair<iterator,iterator> equal_range(const value_type& val);
    pair<multiset<int>::iterator, multiset<int>::iterator> pa = ms.equal_range(3);
    cout<<*(pa.first)<<" "<<*(pa.second)<<endl; // 输出3 4，即后一个迭代器指向后一个位置


    return 0;
}
```
### map
```c++
#include <iostream>
#include <map>

using namespace std;

void print(map<int, int> &mp){
    for(map<int, int>::iterator it=mp.begin(); it!=mp.end(); ++it){
        cout<< it->first << " " << it->second <<endl;
    }
    cout<<endl;
}

void reverse_print(map<int, int> &mp){
    for(map<int, int>::reverse_iterator it=mp.rbegin(); it!=mp.rend(); ++it){
        cout<<it->first<<" => "<<it->second<<endl;
    }
}

int main(){
    map<int, int> mp;
    mp[1] = 1;
    mp[2] = 2;
    mp[3] = 3;
    print(mp);
    reverse_print(mp);

    // 支持的迭代器有:
    // begin(), end(), rbegin(), rend()
    // cbegin(), cend(), crbegin(), crend()

    // empty() 类似
    // size() 类似
    // max_size() 类似

    // insert()
    // pair<iterator,bool> insert(const value_type& val); iterator指向val在map中的位置, bool指示是新插入还是已存在
    // iterator insert(const_iterator position, const value_type& val);
    // void insert (InputIterator first, InputIterator last);
    pair<map<int, int>::iterator, bool> pa = mp.insert(make_pair(1, 2));
    cout<<pa.first->first<<" "<<pa.first->second<<" "<<pa.second<<endl; // 输出1, 1, 0 即(1,2)没有被插入

    /*
    erase()  和set类似
    iterator  erase(const_iterator position);
    size_type erase(const key_type& k);
    iterator  erase(const_iterator first, const_iterator last); */

    // swap()类似
    // clear() 内存释放
    // emplace() 类似

    // 以下和set类似
    // find()
    // count()
    // lower_bound()
    // upper_bound()
    // equal_range()
    return 0;
}
```
### multimap
```c++
#include <iostream>
#include <map>

using namespace std;

void print(multimap<int, int> &mmp){
    for(multimap<int, int>::iterator it=mmp.begin(); it!=mmp.end(); ++it){
        cout<<it->first<<"=>"<<it->second<<endl;
    }
}

int main(){
    multimap<int, int> mmp;
    // 不支持[]操作符

    // 支持的迭代器有:
    // begin(), end(), rbegin(), rend()
    // cbegin(), cend(), crbegin(), crend()

    // empty() 类似
    // size() 类似
    // max_size() 类似

    /*
    insert() 类似multiset
    iterator insert(const value_type& val);
    iterator insert(const_iterator position, const value_type& val);
    void insert (InputIterator first, InputIterator last);*/

    mmp.insert(make_pair(1, 1));
    mmp.insert(make_pair(2, 2));
    mmp.insert(make_pair(3, 3));
    mmp.insert(make_pair(4, 4));
    mmp.insert(make_pair(1, 2333));
    mmp.insert(make_pair(3, 2333));
    print(mmp);

    /*
    erase() 类似
    iterator  erase(const_iterator position);
    size_type erase(const key_type& k);
    iterator  erase(const_iterator first, const_iterator last);
    */

    // swap() 类似
    // clear() 内存释放
    // emplace() 类似

    // find() 和multiset类似
    // cout() 和multisetleisi
    // lower_bound() 和multiset类似
    // upper_bound() 和multiset类似
    // equal_range() 和multiset类似
    return 0;
}
```
### bitset
```c++
#include <iostream>
#include <bitset>

using namespace std;

int main(){
    bitset<16> b1;         // 实例化一个长度为16的全为0的bitset
    bitset<32> b2(0x3f);   // 用0x3f实例化一个bitset
    bitset<16> b3(string("00101111001")); // 用字符串实例化一个bitset
    cout<<b1<<endl;
    cout<<b2<<endl;
    cout<<b3<<endl;

    bitset<16> b4(2333);   // 用10进制数2333实例化一个bitset
    cout<<b4<<endl;

    // size() 返回bitset的长度, 而不是你设置的数的二进制位数
    cout<<"b3's size is: "<<b3.size()<<endl;   // 输出的是16

    // 可以用操作符[]访问信息
    cout<<b3[0]<<endl; // 第0位为对应的2进制的最右边的数

    // count() 返回bitset中1的个数
    size_t ones = b3.count();
    cout<<"b3 has "<<ones<<" ones"<<endl;

    // test() 返回bool值，第pos位为1则为true，为0则为false
    // bool test(size_t pos) const;

    // any() 如果bitset中存在1则返回true，否则返回false
    // bool any() const;
    cout<<b1.any()<<endl;  // 输出0
    cout<<b3.any()<<endl;  // 输出1

    // none() 如果bitset全为0则返回true，否则返回false
    cout<<b1.none()<<endl; // 输出1
    cout<<b3.none()<<endl; // 输出0

    // all() 如果bitset全为1则返回true，否则返回false

    // set()
    //bitset& set(); 将bitset全部置为1
    // bitset& set(size_t pos, bool val = true); 将下标为pos的位置为val, 默认为true
    b1.set();
    cout<<b1<<endl;    // 输出全1
    b3.set(0, 0);      // 将b3最右边那位置为0
    cout<<b3<<endl;

    // reset()
    // bitset& reset();   // 将bitset全置为0
    // bitset& reset(size_t pos); 将bitset下标为pos的位置为0(注意和set()区别)
    b1.reset();
    cout<<b1<<endl;   // 输出全0
    b2.reset(0);      // 将b2最右边那位置为0
    cout<<b2<<endl;

    // flip() 取反
    // bitset& flip();   // bitset整体取反
    // bitset& flip(size_t pos);  // bitset下标为pos的位取反
    b1.flip();
    cout<<b1<<endl;    // 输出全1
    b1.flip(0);        // 将b1下标为0的位取反, 即为0
    cout<<b1<<endl;

    // to_string()   将bitset转换为字符串
    // to_ulong()    转换为unsigned long integer
    // to_ullong()   转换为unsigned long long

    // bitset 可以直接用输入流构造
    /*
    bitset<16> bb;
    cin>>bb;       // 输入01比特流
    */
    return 0;
}
```

---
### algorithm里可能用到的函数
### sort()
```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Point{
    int x, y;
    Point(){}
    Point(int x, int y):x(x), y(y){}
    bool operator<(const Point &rhs)const{
        if(x<rhs.x) return true;
        else if(x==rhs.x) return y<rhs.y;
        else return false;
    }
    friend ostream &operator<<(ostream &os, const Point &p){
        return os<<"("<<p.x<<", "<<p.y<<")";
    }
};

void print(vector<Point> &v){
    for(vector<Point>::iterator it=v.begin(); it!=v.end(); ++it){
        cout<<*it<<endl;
    }
}

int main(){
    vector<Point> v;
    v.emplace_back(1, 2);
    v.emplace_back(1, 1);
    v.emplace_back(2, 1);
    v.emplace_back(3, 4);
    v.emplace_back(2, 0);

    // 将点按x从小到大排序，x相同则将y较小的排在前面
    sort(v.begin(), v.end());
    print(v);

    int arr[] = {5, 4, 2, 1, 199, 233, 2020};
    sort(arr, arr+7);      // 将整个arr数组排序
    //sort(arr, arr+5);    // 将arr前5位进行排序
    for(int i=0; i<7; ++i){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
```

### unique()
```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Point{
    int x, y;
    Point(){}
    Point(int x, int y):x(x), y(y){}

    bool operator<(const Point &rhs)const{
        if(x<rhs.x) return true;
        else if(x==rhs.x) return y<rhs.y;
        else return false;
    }

    bool operator==(const Point &rhs)const{
        return x==rhs.x&&y==rhs.y;
    }

    friend ostream &operator<<(ostream &os, const Point &p){
        return os<<"("<<p.x<<", "<<p.y<<")";
    }
};

void print(vector<Point> &v){
    for(vector<Point>::iterator it=v.begin(); it!=v.end(); ++it){
        cout<<*it<<endl;
    }
}

int main(){
    vector<Point> v;
    v.emplace_back(1, 2);
    v.emplace_back(1, 1);
    v.emplace_back(2, 1);
    v.emplace_back(3, 4);
    v.emplace_back(2, 0);
    v.emplace_back(2, 1);

    // 将点按x从小到大排序，x相同则将y较小的排在前面
    sort(v.begin(), v.end());
    print(v);

    // unique() 必须先排序后再使用, 且需要重载==, 重复的元素将放在末尾(可能会丢失重复的数据?)
    // 返回最后一个不重复的元素的后继元素的迭代器(或者为end)
    vector<Point>::iterator ed = unique(v.begin(), v.end());
    cout<<"去重后:"<<endl;
    for(vector<Point>::iterator it=v.begin(); it!=ed; ++it){
        cout<<*it<<endl;
    }

    int arr[] = {2, 1, -1, 2, 2, 5, 4, 5, 7};
    sort(arr, arr+9);
    cout<<"排序后:"<<endl;
    for(int i=0; i<9; ++i){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    int idx = unique(arr, arr+9) - arr;
    cout<<"去重后:"<<endl;
    for(int i=0; i<idx; ++i){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
```

### nth_element()
```c++
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main(){
    int arr[] = {4, 1, 10, -1, 6, 7};   // 若排序为, -1, 1, 4, 6, 7, 10

    // void nth_element(RandomAccessIterator first, RandomAccessIterator nth, RandomAccessIterator last);
    // 指的是迭代器nth所指的那个元素放到了最终位置
    nth_element(arr, arr+3, arr+6); // 下标为3即第4个元素为排序后第4大
    cout<<arr[3]<<endl;             // 输出6

    nth_element(arr, arr+3, arr+6, greater<int>());  // 传入cmp, 逆序下nth
    cout<<arr[3]<<endl;      // 逆序下第4个，即为4

    return 0;
}
```

### prev_permutation()
```c++
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    // prev_permutation()  要求元素重载小于号，或者传入cmp
    // bool prev_permutation (BidirectionalIterator first, BidirectionalIterator last );
    // bool prev_permutation (BidirectionalIterator first, BidirectionalIterator last, Compare comp);

    int arr[] = {1, 2, 3, 4};
    reverse(arr, arr+4);         // 逆置为4, 3, 2, 1

    do{
        for(int i=0; i<4; ++i){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }while(prev_permutation(arr, arr+4));

    cout<<"再次输出arr[]:"<<endl;   // 排列后恢复原状，即恢复为4, 3, 2, 1
    for(int i=0; i<4; ++i){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    reverse(arr, arr+4);          // 再次逆置为1, 2, 3, 4
    // 使用降序来获取前一个排列
    do{
        for(int i=0; i<4; ++i){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }while(prev_permutation(arr, arr+4, greater<int>()));
    return 0;
}
```

### next_permutation()
```c++
与prev_permutaion()类似
```

### lower_bound()
```c++
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int A[10] = {1, 2, 3, 3, 3, 4, 4, 6, 7, 9};

    // 找到3，返回最左边位置，即idx_1=2
    int idx_1 = lower_bound(A, A+10, 3) - A;
    cout<<idx_1<<endl;

    // 没找到5，返回第一个大于5的数的位置，即idx_2=7
    int idx_2 = lower_bound(A, A+10, 5) - A;
    cout<<idx_2<<endl;
    return 0;
}
```

### upper_bound()
```c++
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int A[10] = {1, 2, 3, 3, 3, 4, 4, 6, 7, 9};

    // 找到3，返回最右边位置的后一元素的下标，即idx_1=5
    int idx_1 = upper_bound(A, A+10, 3) - A;
    cout<<idx_1<<endl;

    // 没找到5，返回第一个大于5的数的位置，即idx_2=7
    int idx_2 = upper_bound(A, A+10, 5) - A;
    cout<<idx_2<<endl;
    return 0;
}
```