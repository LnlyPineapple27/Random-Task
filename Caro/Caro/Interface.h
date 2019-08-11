#pragma once
#include "Board.h"\
#define H_OFFSET 3
#define W_OFFSET 10
struct Map {
	int col, line;
};
class Interface 
{
private:
	unsigned int _height, _width;
	char _p1, _p2;
	int _color;
	Board* _board;
	Map _cursor;

private:
	Map getLoca(Loca place);
	void printCursor(Loca NextPlace);
	void eraseCursor(Loca prevPlace);
public:
	Interface();
	~Interface();

public:
	void DrawBoard();


};

