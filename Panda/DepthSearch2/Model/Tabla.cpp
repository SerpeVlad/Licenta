#include "../Headers/Model/Tabla.h"
#include <sstream>

std::vector<std::vector<Piesa>> Tabla::getBoard()
{
	return this->Board;
}

void Tabla::setBoard(std::vector<std::vector<Piesa>> board)
{
	this->Board = board;
}

std::string Tabla::getFen()
{
	return this->fen;
}

void Tabla::setFen(std::string fen)
{
	this->fen = fen;
}

int Tabla::getHowMoves()
{
	return this->howMoves;
}

void Tabla::setHowMoves(int howMoves)
{
	this->howMoves = howMoves;
}

std::vector<Piesa> Tabla::getLstPiese()
{
	return this->lstPiese;
}

void Tabla::setLstPiese(std::vector<Piesa> lst)
{
	this->lstPiese = lst;
}

std::vector<Piesa> Tabla::getLstPieseAlb()
{
	return this->lstPieseAlb;
}

void Tabla::setLstPieseAlb(std::vector<Piesa> lst)
{
	this->lstPieseAlb = lst;
}

std::vector<Piesa> Tabla::getLstPieseNegru()
{
	return this->lstPieseNegru;
}

void Tabla::setLstPieseNegru(std::vector<Piesa> lst)
{
	this->lstPieseNegru = lst;
}

std::vector<std::pair<std::pair<int, int>, Piesa>> Tabla::getListMoves()
{
	if (getHowMoves() == 1) {// muta alb
		std::vector<std::pair<std::pair<int, int>, Piesa>> lst = std::vector<std::pair<std::pair<int, int>, Piesa>>();
		std::vector<Piesa> l = getLstPieseAlb();
		for (int i = 0;i < l.size();i++) {
			l[i].makeLstMoves();
			std::vector<std::pair<int, int>> lst_moves = l[i].getLstMoves();
			for (int j = 0;j < lst_moves.size();j++) {
				if(verifyMoveIsValid(l[i], lst_moves[j]))
					lst.push_back(std::pair<std::pair<int, int>, Piesa>(lst_moves[j], l[i]));
			}
			if(l[i].getType() == "pion"){
				if(getBoard()[l[i].getX()][l[i].getY() + 1].getColor() == 0){
					if(verifyMoveIsValid(l[i], std::pair<int, int>(l[i].getX(), l[i].getY() + 1))){
						lst.push_back(std::pair<std::pair<int, int>, Piesa>(std::pair<int, int>(l[i].getX(), l[i].getY() + 1), l[i]));
						l[i].addMove(std::pair<int, int>(l[i].getX(), l[i].getY() + 1));
					}
				}
				if(getBoard()[l[i].getX()][l[i].getY() - 1].getColor() == 0){
					if(verifyMoveIsValid(l[i], std::pair<int, int>(l[i].getX(), l[i].getY() - 1))){
						lst.push_back(std::pair<std::pair<int, int>, Piesa>(std::pair<int, int>(l[i].getX(), l[i].getY() - 1), l[i]));
						l[i].addMove(std::pair<int, int>(l[i].getX(), l[i].getY() - 1));
					}
				}
			} //mai trebuie en Passant
		}
		return lst;
	}
	else { //muta negru HowMoves = 0
		std::vector<std::pair<std::pair<int, int>, Piesa>> lst = std::vector<std::pair<std::pair<int, int>, Piesa>>();
		std::vector<Piesa> l = getLstPieseNegru();
		for (int i = 0;i < l.size();i++) {
			l[i].makeLstMoves();
			std::vector<std::pair<int, int>> lst_moves = l[i].getLstMoves();
			for (int j = 0;j < lst_moves.size();j++) {
				if(verifyMoveIsValid(l[i], lst_moves[j]))
					lst.push_back(std::pair<std::pair<int, int>, Piesa>(lst_moves[j], l[i]));
			}
			if(l[i].getType() == "pion"){
				if(getBoard()[l[i].getX()][l[i].getY() + 1].getColor() == 1){
					if(verifyMoveIsValid(l[i], std::pair<int, int>(l[i].getX(), l[i].getY() + 1))){
						lst.push_back(std::pair<std::pair<int, int>, Piesa>(std::pair<int, int>(l[i].getX(), l[i].getY() + 1), l[i]));
						l[i].addMove(std::pair<int, int>(l[i].getX(), l[i].getY() + 1));
					}
				}
				if(getBoard()[l[i].getX()][l[i].getY() - 1].getColor() == 1){
					if(verifyMoveIsValid(l[i], std::pair<int, int>(l[i].getX(), l[i].getY() - 1))){
						lst.push_back(std::pair<std::pair<int, int>, Piesa>(std::pair<int, int>(l[i].getX(), l[i].getY() - 1), l[i]));
						l[i].addMove(std::pair<int, int>(l[i].getX(), l[i].getY() - 1));
					}
				}
			} //mai trebuie en Passant
		}
		return lst;
	}
}

void Tabla::extractInfoFromFen()
{
    std::istringstream iss(fen);
    std::string board, turn, castling, enpassant, halfmove, fullmove;
    iss >> board >> turn >> castling >> enpassant >> halfmove >> fullmove;

	std::vector<std::vector<Piesa>> Board(8, std::vector<Piesa>(8));
	std::vector<Piesa> lstPiese;
	std::vector<Piesa> lstPieseAlb;
	std::vector<Piesa> lstPieseNegru;
    this->howMoves = (turn == "w") ? 1 : 0;
	int y = 0;
	int x = 0;
	int id = 0;
	int xa, ya, xn, yn;
    for (char c : board) {
        if (c == '/') {
			y++; 
			x = 0;
			continue;
		} 
		if (isdigit(c)) {
			x += c - '0'; 
			continue;
		}
		Piesa piece;
		switch (c) {
			case 'p':
				piece = Pion(id, x, y, 1, 0); 
				lstPieseNegru.push_back(piece);
				lstPiese.push_back(piece);
				break; 
			case 'r': piece = Tura(id, x, y, 5, 0); lstPiese.push_back(piece); lstPieseNegru.push_back(piece); break; // Rook
			case 'n': piece = Cal(id, x, y, 3, 0); lstPiese.push_back(piece); lstPieseNegru.push_back(piece); break; // Knight
			case 'b': piece = Nebun(id, x, y, 3, 0); lstPiese.push_back(piece); lstPieseNegru.push_back(piece); break; // Bishop
			case 'q': piece = Regina(id, x, y, 9, 0); lstPiese.push_back(piece); lstPieseNegru.push_back(piece); break; // Queen
			case 'k': 
				piece = Rege(id, x, y, 0, 0); 
				lstPieseNegru.push_back(piece);
				lstPiese.push_back(piece);
				for(char c: castling) {
					if(c == 'k') piece.setK(true);
					if(c == 'q') piece.setQ(true);
				}
				xn = x;
				yn = y;
				break; 
			case 'P': 
				piece = Pion(id, x, y, 1, 1); 
				lstPieseAlb.push_back(piece);
				lstPiese.push_back(piece);
				break; 
			case 'R': piece = Tura(id, x, y, 5, 1); lstPiese.push_back(piece); lstPieseAlb.push_back(piece); break; // Rook
			case 'N': piece = Cal(id, x, y, 3, 1); lstPiese.push_back(piece); lstPieseAlb.push_back(piece); break; // Knight
			case 'B': piece = Nebun(id, x, y, 3, 1); lstPiese.push_back(piece); lstPieseAlb.push_back(piece); break; // Bishop
			case 'Q': piece = Regina(id, x, y, 9, 1); lstPiese.push_back(piece); lstPieseAlb.push_back(piece); break; // Queen
			case 'K': 
				piece = Rege(id, x, y, 0, 1); 
				lstPieseAlb.push_back(piece);
				lstPiese.push_back(piece);
				for(char c: castling) {
					if(c == 'K') piece.setK(true);
					if(c == 'Q') piece.setQ(true);
				}
				xa = x;
				ya = y;
				break; 
		}
		Board[y][x] = piece;
		id++;
		x++;
    }
	setBoard(Board);
	setLstPiese(lstPiese);
	setLstPieseAlb(lstPieseAlb);
	setLstPieseNegru(lstPieseNegru);
	//add absolute pin 
	//to do
}

bool Tabla::verifyMoveIsValid(Piesa piece, std::pair<int, int> move) {
	if (move.first < 0 || move.first >= 8 || move.second < 0 || move.second >= 8) {
		return false;
	}
	//to do
	
	return true;
}
