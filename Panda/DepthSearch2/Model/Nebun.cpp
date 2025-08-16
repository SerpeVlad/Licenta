#include "Nebun.h"

std::vector<std::pair<int, int>> Nebun::makeLstMoves() {
	if (getAbsolutePin() == false) {
		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();

		int YMove = 1;
		for (int i = getX();i < 8;i++) {
			if (YMove + getY() < 8) {
				std::pair<int, int> move = std::pair<int, int>(i, getY() + YMove);
				lst.push_back(move);
				YMove++;
			}
			else
				break;

		}
		for (int i = 0; i <= lst.size();i++) {
			dic[lst[i]] = YMove;
		}
		int WhereToJump = YMove;

		int YMove = 1;
		for (int i = getX();i >= 0;i--) {
			if (YMove + getY() < 8) {
				std::pair<int, int> move = std::pair<int, int>(i, getY() + YMove);
				lst.push_back(move);
				YMove++;
			}
			else
				break;
		}
		for (int i = WhereToJump; i <= lst.size();i++) {
			dic[lst[i]] = YMove += WhereToJump;
		}
		WhereToJump += YMove;

		int YMove = 1;
		for (int i = getX();i < 8;i++) {
			if (getY() - YMove >= 0) {
				std::pair<int, int> move = std::pair<int, int>(i, getY() - YMove);
				lst.push_back(move);
				YMove++;
			}
			else
				break;
		}
		for (int i = WhereToJump; i <= lst.size();i++) {
			dic[lst[i]] = WhereToJump + YMove;
		}
		WhereToJump += YMove;

		int YMove = 1;
		for (int i = getX();i >= 0;i--) {
			if (getY() - YMove >= 0) {
				std::pair<int, int> move = std::pair<int, int>(i, getY() - YMove);
				lst.push_back(move);
				YMove++;
			}
			else
				break;
		}
		for (int i = WhereToJump; i <= lst.size();i++) {
			dic[lst[i]] = WhereToJump + YMove;
		}
		WhereToJump += YMove;

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
