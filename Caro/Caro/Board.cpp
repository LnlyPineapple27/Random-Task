#include "Board.h"


Board::Board() {
	m_width = 5;
	m_height = 5;
	m_loca = { 0,0 };
	clearBoard();
}
Board::Board( int height,  int width) {
	m_width = width;
	m_height = height;
	m_loca = { 0,0 };
	clearBoard();
}
Board::~Board() {
	//nothing to do here :[
}

//=====================
void Board::clearBoard() {
	//m_board.resize(m_height);
	//for (int i = 0; i < m_board.size(); i++) {
	//	m_board.resize(i,m_width);
	//	/*for (int j = 0; j < m_board[i].size(); j++) {
	//		m_board[i][j] = 0;
	//	}*/
	//}
	m_board.resize(m_height, vector<int>(m_width));
}

void Board::printBit() {

	for (int i = 0; i < m_board.size(); i++) {
		for (int j = 0; j < m_board[i].size(); j++) {
			cout << m_board[i][j] << " ";
		}
		cout << endl;
	}
}

Board& Board::operator=(const Board& other) {
	m_board = other.m_board;
	m_height = other.m_height;
	return *this;
}
//
//int Board::checkWIN(Loca loca) {
//	//check player1
//	if (check(loca, P1))
//		return 1;
//	
//	//check player2
//	if (check(loca, P2))
//		return 2;
//
//	return 0;
//}

bool Board::check(Loca loca, Player player) {
	int p;
	if (player == P1)
		p = 1;
	else if (player == P2)
		p = 2;
	else return false;//invalid input

	int count;
	//ngang
	count = 0;
	for (int i = 0; i < 5; i++) {
		if (loca.col + i >= m_width)
			break;
		else {
			//cout << "TEST: " << loca.col + i;
			if (m_board[loca.line][loca.col + i] == p)
				++count;
			else break;
		}
	}
	for (int i = 0; i < 5; i++) {
		if (loca.col - i < 0)
			break;
		else {
			//cout << "TEST: " << loca.col - i;
			if (m_board[loca.line][loca.col - i] == p)
				++count;
			else break;
		}
	}

	if (count > 5)
		return 1;

	//doc
	count = 0;
	for (int i = 0; i < 5; i++) {
		if (loca.line + i >= m_height)
			break;

		if (m_board[loca.line + i][loca.col] == p)
			++count;
		else break;
	}
	for (int i = 0; i < 5; i++) {
		if (loca.line - i < 0)
			break;
		
		if (m_board[loca.line - i][loca.col] == p)
			++count;
		else break;
	}

	if (count > 5)
		return 1;

	//cheo chinh
	count = 0;
	for (int i = 0; i < 5; i++) {
		if ((loca.line + i >= m_height) || (loca.col + i >= m_width))
			break;

		if (m_board[loca.line + i][loca.col + i] == p)
			++count;
		else break;
	}
	for (int i = 0; i < 5; i++) {
		if ((loca.line - i < 0) || (loca.col - i < 0))
			break;

		if (m_board[loca.line - i][loca.col - i] == p)
			++count;
		else break;
	}

	if (count > 5)
		return 1;

	//cheo phu
	count = 0;
	for (int i = 0; i < 5; i++) {
		if ((loca.line - i < 0) || (loca.col + i >= m_width))
			break;

		if (m_board[loca.line - i][loca.col + i] == p)
			++count;
		else break;
	}
	for (int i = 0; i < 5; i++) {
		if ((loca.line + i >= m_height) || (loca.col - i < 0))
			break;

		if (m_board[loca.line + i][loca.col - i] == p)
			++count;
		else break;
	}

	if (count > 5)
		return 1;

	return 0;
}

bool Board::InputBoard(Loca loca, Player p) {

	if (m_board[loca.line][loca.col] != 0)
		return 0;//Slot was taken

	if (p == P1) {
		m_board[loca.line][loca.col] = 1;
		return 1;
	}
	else if (p == P2) {
		m_board[loca.line][loca.col] = 2;
		return 1;
	}


	return 0;
}
