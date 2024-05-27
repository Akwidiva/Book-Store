#ifndef MAINBOOKDETAILS_PY
#define MAINBOOKDETAILS_PY

#include <QDialog>

namespace Ui {
    class bookdetails;
}

class bookdetails : public QDialog
{
    Q_OBJECT

public:
    explicit bookdetails(QWidget *parent = nullptr);
    ~bookdetails();

private:
    Ui::bookdetails *ui;
};

#endif // MAINBOOKDETAILS_PY
