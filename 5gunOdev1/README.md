@pytest.fixture: Bu dekoratör, test fonksiyonlarında kullanılabilen ve önceden tanımlanmış bir nesne veya fonksiyonu döndürür. Bu nesneler, bir testin belirli bir koşulda çalışmasına izin verir.

@pytest.mark.parametrize: Bu dekoratör, bir test fonksiyonunu bir dizi farklı parametreyle çalıştırmak için kullanılır. Bu dekoratör, test fonksiyonunu, belirtilen parametrelerle ayrı ayrı çalıştırır.

@pytest.mark.skip: Bu dekoratör, bir testin belirli bir koşulda atlanması gerektiğinde kullanılır. Bu dekoratör, test fonksiyonunu atlar ve sonuçları göz ardı eder.

@pytest.mark.xfail: Bu dekoratör, bir testin beklenen bir şekilde başarısız olması durumunda kullanılır. Bu dekoratör, testin hala çalışmasına izin verir, ancak başarısız olması durumunda sonucu dikkate almaz.

@pytest.mark.timeout: Bu dekoratör, bir testin belirli bir sürede tamamlanması gerektiğinde kullanılır. Bu dekoratör, belirtilen süre içinde tamamlanmayan testler için bir hata fırlatır.