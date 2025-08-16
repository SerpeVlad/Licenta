#include "Tura.h"

std::vector<std::pair<int, int>> Tura::makeLstMoves() {
	if (getAbsolutePin() == false) {
		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();

		for (int i = getX();i < 8;i++) {
				std::pair<int, int> move = std::pair<int, int>(i, getY());
				lst.push_back(move);
		}
		for (int i = 0; i <= lst.size();i++) {
			dic[lst[i]] = lst.size();
		}

		int lastMove = lst.size();
		for (int i = getX();i >= 0;i--) {
			std::pair<int, int> move = std::pair<int, int>(i, getY());
			lst.push_back(move);
		}
		for (int i = lastMove; i <= lst.size();i++) {
			dic[lst[i]] = lst.size();
		}

		lastMove = lst.size();
		for (int i = getY();i < 8;i++) {
			std::pair<int, int> move = std::pair<int, int>(getX(), i);
			lst.push_back(move);
	
		}
		for (int i = lastMove; i <= lst.size();i++) {
			dic[lst[i]] = lst.size();
		}

		lastMove = lst.size();
		for (int i = getY();i >= 0;i--) {
			std::pair<int, int> move = std::pair<int, int>(getX(), i);
			lst.push_back(move);
				
		}
		for (int i = lastMove; i <= lst.size();i++) {
			dic[lst[i]] = lst.size();
		}

		setWhereToLookIfPathBlocked(dic);
		setLstMoves(lst);
		return lst;
	}
	else {

		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();
		setWhereToLookIfPathBlocked(dic);
		setLstMoves(lst);
		return lst;
	}

}
