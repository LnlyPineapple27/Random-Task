#include "Interface.h"

Interface::Interface() {
	_height = 15;
	_width = 30;
	_p1 = 'X';
	_p2 = 'O';
	_color = Color_Cyan;
	_cursor.m_x = 1;
	_cursor.m_y = 1;
	_count = 0;
	_board = new Board(_height, _width);
	//_board->clearBoard();
}
Interface::~Interface() {
	if (_board != nullptr)
		delete _board;
}

//------------------------
Loca Interface::getLoca() {
	/*Loca res;
	res.col = (_cursor.m_x-1) / 2;
	res.line = _cursor.m_y-1;
	return res;*/
	return { (_cursor.m_x - 1) / 2 ,_cursor.m_y - 1 };
}
void Interface::showLoca() {
	gotoXY(0, 0);
	Loca p = getLoca();
	if (p.col < 10) cout << '0' << p.col;
	else cout << p.col;

	cout << " - ";
	
	if (p.line < 10) cout << '0' << p.line;
	else cout << p.line;
}
void Interface::printCursor(Map NextPlace) {
	showLoca();
	TextColor(_color);
	gotoXY(NextPlace.m_x - 1, NextPlace.m_y);
	cout << '[';
	gotoXY(NextPlace.m_x + 1, NextPlace.m_y);
	cout << ']';
	gotoXY(NextPlace.m_x, NextPlace.m_y);
	TextColor(default_Color);
}

void Interface::eraseCursor(Map prevPlace) {
	gotoXY(prevPlace.m_x - 1, prevPlace.m_y);
	cout << " ";
	gotoXY(prevPlace.m_x + 1, prevPlace.m_y);
	cout << " ";
	//gotoXY(place.col + 1, place.line);
	//cout << ' ';
}
//-------------------------------
void Interface::DrawBoard() {
	for (int i = 0; i < _height; ++i) {
		cout << "\n";
		for (int j = 0; j < _width; ++j) {
			cout << " .";
		}
	}
}

void Interface::Start() {
	DrawBoard();
	printCursor(_cursor);
	//while(1)
	doTask();
	
}

void Interface::doTask() {
	char key = getch();

	if (key == KEY_ESC)//undo
		return;
	else if (key == KEY_UP) {
		eraseCursor(_cursor);
		if (_cursor.m_y == 1) {
			_cursor.m_y = _height;
		}
		else {
			--_cursor.m_y;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_DOWN) {
		eraseCursor(_cursor);
		if (_cursor.m_y == _height) {
			_cursor.m_y = 1;
		}
		else {
			++_cursor.m_y;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_LEFT) {
		eraseCursor(_cursor);
		if (_cursor.m_x == 1) {
			_cursor.m_x = 2 * _width - 1;
		}
		else {
			_cursor.m_x -= 2;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_RIGHT) {
		eraseCursor(_cursor);
		if (_cursor.m_x == 2 * _width - 1) {
			_cursor.m_x = 1;
		}
		else {
			_cursor.m_x += 2;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_SPACE || key == KEY_ENTER) {
		drawXO();
	}
	return doTask();
}

void Interface::drawXO() {
	Loca loca = getLoca();
	bool input = 0;
	if (_count % 2 == 0)
		input = _board->InputBoard(loca, P1);
	else
		input = _board->InputBoard(loca, P2);

	if (!input) {
		gotoXY(20, 0);
		cout << "Slot has been taken";// ~or sth went wrong : |
	}
	else {
		gotoXY(20, 0);
		cout << "                   ";
		++_count;


		//Draw XO on board
		gotoXY(_cursor.m_x, _cursor.m_y);

		if (_count % 2 == 0)
			cout << _p1;
		else 
			cout << _p2;

		gotoXY(_cursor.m_x, _cursor.m_y);
	}
}