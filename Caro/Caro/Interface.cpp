#include "Interface.h"

Interface::Interface() {
	_height = 20;
	_width = 35;
	_p1 = 'X';
	_p2 = 'O';
	_color1 = Color_Red;
	_color2 = Color_Green;
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
	TextColor(Color_Yellow);
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
	char key = _getch();

	if (key == KEY_ESC) {//Exit
		clrscr();
		return;
	}
	else if (key == KEY_UP || key == 'w' || key == 'W') {
		eraseCursor(_cursor);
		if (_cursor.m_y == 1) {
			_cursor.m_y = _height;
		}
		else {
			--_cursor.m_y;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_DOWN || key == 's' || key == 'S') {
		eraseCursor(_cursor);
		if (_cursor.m_y == _height) {
			_cursor.m_y = 1;
		}
		else {
			++_cursor.m_y;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_LEFT || key == 'a' || key == 'A') {
		eraseCursor(_cursor);
		if (_cursor.m_x == 1) {
			_cursor.m_x = 2 * _width - 1;
		}
		else {
			_cursor.m_x -= 2;
		}
		printCursor(_cursor);
	}
	else if (key == KEY_RIGHT || key == 'd' || key == 'D') {
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
		
		int res = drawXO();

		gotoXY(20, 0);
		if (res == 1) {
			cout << "Player " << _p1 << " has won         ";
		}
		else if (res == 2)
			cout << "Player " << _p2 << " has won         ";

		if (res != 0) {
			system("pause>nul");
			clrscr();
			return;
		}
	}
	return doTask();
}

int Interface::drawXO() {
	Loca loca = getLoca();
	bool input = 0;
	Player p;
	if (_count % 2 != 0)
		p = P1;
	else
		p = P2;

	input = _board->InputBoard(loca, p);


	if (!input) {
		gotoXY(20, 0); 
		cout << "Slot has been taken               ";// ~or sth went wrong : |
		return 0;
	}
	gotoXY(20, 0);
	cout << "Inputed at slot " << loca.col << "-" << loca.line<<"                   ";
	++_count;


	//Draw XO on board
	gotoXY(_cursor.m_x, _cursor.m_y);

	if (p == P1) {
		TextColor(_color1);
		cout << _p1;
	}
	else {
		TextColor(_color2);
		cout << _p2;
	}

	TextColor(default_Color);
	gotoXY(_cursor.m_x, _cursor.m_y);

	if (_board->check(loca, p)) {
		if (p == P1)
			return 1;
		else
			return 2;
	}

	return 0;
}