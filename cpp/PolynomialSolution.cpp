typedef  struct PolyNode *Polynomial;
struct PolyNode {
	int coef;
	int expon;
	Polynomial link;
};
void Attach(int c, int e, Polynomial *pRear)
{
	Polynomial P;

	P = (Polynomial)malloc(sizeof(struct PolyNode));
	P->coef = c;
	P->expon = e;
	P->link = NULL;
	(*pRear)->link = P;
	*pRear = P;


}

Polynomial ReadPoly()
{
	Polynomial  P, Rear, t;
	int c, e, N;

	scanf("%d", &N);
	P = (Polynomial)malloc(sizeof(struct PolyNode));
	P->link = NULL;
	Rear = P;
	while (N--) {
		scanf("%d %d", &c, &e);
		Attach(c, e, &Rear);
	}
	t = P; P = P->link; free(t);
	return P;
		
}