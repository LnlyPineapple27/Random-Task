#pragma once
#include "Console.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Loca {
	unsigned int m_x, m_y;
};

class Board
{
private:
	vector<vector<bool>> m_board;
	unsigned int m_height, m_width;

public:
	Loca m_loca;

public:
	Board();
	Board(unsigned int height, unsigned int width);
	Board& operator=(const Board& other);
	~Board();

public:
	void clearBoard();
	bool checkWIN(Loca location);
	void printBit();


};

