#pragma once
#include "Console.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Loca {
	int col, line;//virtual map
};

enum Player {
	P1 = 1,
	P2 = 2,
	NONE = 0
};

class Board
{
private:
	vector<vector<int>> m_board;
	 int m_height, m_width;

public:
	Loca m_loca;

public:
	Board();
	Board( int height,  int width);
	Board& operator=(const Board& other);
	~Board();

public:
	void clearBoard();
	//int checkWIN(Loca loca);
	bool check(Loca loca, Player player);
	void printBit();
	bool InputBoard(Loca loca,Player p);

};

