#include "Interface.h"

Interface::Interface() {
	_height = 10;
	_width = 10;
	_p1 = 'X';
	_p2 = 'O';
	_color = Color_Cyan;
	_board = new Board(_height, _width);
	_board->clearBoard();
}
Interface::~Interface() {
	if (_board != nullptr)
		delete _board;
}

//------------------------
Map Interface::getLoca(Loca place) {

	return { 0,0 };
}

void Interface::printCursor(Loca NextPlace) {
	Map place = getLoca(NextPlace);
	TextColor(_color);
	gotoXY(place.col - 1, place.line);
	cout << '[';
	gotoXY(place.col + 1, place.line);
	cout << ']';
	TextColor(default_Color);
}

void Interface::eraseCursor(Loca prevPlace) {
	Map place = getLoca(prevPlace);
	gotoXY(place.col - 1, place.line);
	cout << " . ";
	//gotoXY(place.col + 1, place.line);
	//cout << ' ';
}
//-------------------------------
void Interface::DrawBoard() {
	for (int i = 0; i < _height; ++i) {
		for (int j = 0; j < _width; ++j) {
			cout << " .";
		}
		cout << "\n";
	}
}
