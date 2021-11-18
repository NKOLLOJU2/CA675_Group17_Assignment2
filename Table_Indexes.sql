CREATE INDEX BookIdCategoryIndx ON Book_Category (book_id);
CREATE INDEX AutIdIndx on Author(author_id);
CREATE INDEX CategoryIndex on Categories (category_id);
CREATE INDEX BookAuthIdIndex on Book_Author(author_id);
CREATE INDEX BookId_AuthIndex on Book_Author(book_id);
CREATE INDEX BookCategoryIdIndx ON Book_Category (category_id);