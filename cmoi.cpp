#include <iostream>
using namespace std;
int main() {
    int numScores;
    std::cout << "Nhập số lượng điểm số: ";
    std::cin >> numScores;
    int totalScore = 0;
    for (int i = 0; i < numScores; ++i) {
        int score;
        std::cout << "Nhập điểm số thứ " << i + 1 << ": ";
        std::cin >> score;
        totalScore += score;
    }
    double averageScore = static_cast<double>(totalScore) / numScores;
    std::cout << "Điểm trung bình: " << averageScore << std::endl;
    return 0;
}
