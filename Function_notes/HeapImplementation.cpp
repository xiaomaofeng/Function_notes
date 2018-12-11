#ifndef HEAP_H
#define HEAP_H

#include <algorithm>
#include <functional>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>
template <typename T, typename TComparator = std::equal_to<T>,
	typename PComparator = std::less<double>,
	typename Hasher = std::hash<T> >
	class Heap {
	public:
		/// Constructs an m-ary heap. M should be >= 2
		Heap(int m = 2, const PComparator &c = PComparator(),
			const Hasher &hash = Hasher(), const TComparator &tcomp = TComparator());

		/// Destructor as needed
		~Heap();

		/// Adds an item with the provided priority
		void push(double pri, const T &item);

		/// returns the element at the top of the heap
		///  max (if max-heap) or min (if min-heap)
		T const &top() const;

		/// Removes the top element
		void pop();

		/// returns true if the heap is empty
		bool empty() const;

		/// decreaseKey reduces the current priority of
		/// item to newpri, moving it up in the heap
		/// as appropriate.
		void decreaseKey(double newpri, const T &item);

	private:
		/// Add whatever helper functions you need below
		void trickleUp(int loc);
		void trickleDown(int loc);

		// These should be all the data members you need.
		std::vector<std::pair<double, T> > store_;
		int m_;   // degree
		PComparator c_;
		std::unordered_map<T, size_t, Hasher, TComparator> keyToLocation_;
};

// Complete
template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	Heap<T, TComparator, PComparator, Hasher>::Heap(int m, const PComparator &c,
		const Hasher &hash,
		const TComparator &tcomp)
	: store_(), m_(m), c_(c), keyToLocation_(100, hash, tcomp) {
}

// Complete
template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	Heap<T, TComparator, PComparator, Hasher>::~Heap() {
}

template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	void Heap<T, TComparator, PComparator, Hasher>::push(double priority,
		const T &item) {
	// You complete.
	std::pair<double, T> temp(priority, item);
	store_.push_back(temp);
	keyToLocation_[item] = store_.size();
	// insert(std::make_pair(item, store_.size()));
	trickleUp(store_.size() - 1);
}

template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	void Heap<T, TComparator, PComparator, Hasher>::trickleUp(int loc) {
	int parent = (loc - 1) / m_;
	while (parent >= 0 && c_(store_[loc].first, store_[parent].first)) {
		//swap loc with parent
		std::pair<double, T> temp = store_[loc];
		store_[loc] = store_[parent];
		store_[parent] = temp;
		double to_swap = keyToLocation_[store_[loc].second];
		keyToLocation_[store_[loc].second] = keyToLocation_[store_[parent].second];
		keyToLocation_[store_[parent].second] = to_swap;
		loc = parent;
		parent = (loc - 1) / m_;
	}
}


template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	void Heap<T, TComparator, PComparator, Hasher>::decreaseKey(double priority,
		const T &item) {
	std::pair<double, T> temp = store_[keyToLocation_[item]];
	temp.first = priority;
	trickleUp(keyToLocation_[item]);
}

template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	T const &Heap<T, TComparator, PComparator, Hasher>::top() const {
	// Here we use exceptions to handle the case of trying
	// to access the top element of an empty heap
	if (empty()) {
		throw std::logic_error("can't top an empty heap");
	}
	return store_[0].second;
}

/// Removes the top element
template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	void Heap<T, TComparator, PComparator, Hasher>::pop() {
	if (empty()) {
		throw std::logic_error("can't pop an empty heap");
	}
	store_[0] = store_[store_.size() - 1];
	keyToLocation_.erase(store_[0].second);
	store_.pop_back();
	if (empty()) return;
	trickleDown(0);
}
template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	void Heap<T, TComparator, PComparator, Hasher>::trickleDown(int loc) {
	if (loc*m_ + 1 > store_.size() - 1) return;
	int smallerChild = m_ * loc + 1; // start w/ left
	for (size_t i = 1; i < m_; i++) {
		if (m_*loc + i < store_.size()) {//if the right exist
			int rChild = m_ * loc + i + 1;
			if (c_(store_[rChild].first, store_[smallerChild].first)) {
				smallerChild = rChild;
			}
		}
	}
	if (c_(store_[smallerChild].first, store_[loc].first)) {
		//swap smallerChild and loc
		std::pair<double, T> temp = store_[loc];
		store_[loc] = store_[smallerChild];
		store_[smallerChild] = temp;
		double to_swap = keyToLocation_[store_[loc].second];
		keyToLocation_[store_[loc].second] = keyToLocation_[store_[smallerChild].second];
		keyToLocation_[store_[smallerChild].second] = to_swap;
		trickleDown(smallerChild);
	}
}


/// returns true if the heap is empty
template <typename T, typename TComparator, typename PComparator,
	typename Hasher>
	bool Heap<T, TComparator, PComparator, Hasher>::empty() const {
	return store_.empty();
}

#endif