#include "Board.h"


Board::Board() {
	m_width = 5;
	m_height = 5;
	m_loca = { 0,0 };
	//clearBoard();
}
Board::Board(unsigned int height, unsigned int width) {
	if (width > m_width)
		m_width = width;
	if (height > m_height)
		m_height = height;
	m_loca = { 0,0 };
	//clearBoard();
}
Board::~Board() {

}

//=====================
void Board::clearBoard() {
	m_board.resize(m_height);
	for (int i = 0; i < m_board.size(); ++i) {
		m_board[i].resize(m_width);
		for (int j = 0; j < m_board[i].size(); ++j) {
			m_board[i][j] = 0;
		}
	}
}

void Board::printBit() {

	for (int i = 0; i < m_board.size(); ++i) {
		for (int j = 0; j < m_board[i].size(); ++j) {
			cout << m_board[i][j] << " ";
		}
		cout << endl;
	}
}

Board& Board::operator=(const Board& other) {
	m_board = other.m_board;
	m_height = other.m_height;
}

bool Board::checkWIN(Loca location) {

	return 0;
}

