CREATE DATABASE localidades;

USE DATABASE localidades;

CREAT TABLE tb_microrregiao (
      id INT PRIMARY KEY ,
      nome varchar(50),  
);


INSERT INTO tb_microrregiao (id, nome)
VALUES(
    (8, "Itapipoca"),
    (9,"Baixo Curu"),
    (10,"Uruburetama"),
    (11,"Médio Curu"),
    (12,"Canindé"),
    (13,"Baturité"),
    (14,"Chorozinho"),
    (15, "Cascavel"),
);

CREAT TABLE tb_municipios (
      id INT PRIMARY KEY AUTO_INCREMENT,
      nome varchar(50),
      latitude varchar(50),
      longitude varchar(50),
      FOREIGN KEY (id_microrregiao) REFERENCES tb_municipios(id)
);


INSERT INTO tb_municipios (nome, latitude, longitude, id_microrregiao) VALUES(
    ("Amontada", "-3.3632839", "-39.827957", 8),
    ("Itapiúna", "-4.549090", "-38.928910", 13),
    ("Palmácia", "-4.137940", "-38.842450", 13),
    ("Trairi", "-3.265893", "-39.274583", 8),
    ("Paracuru", "-3.408865", "-39.029867", 9),
    ("Paraipaba", "-3.437627", "-39.148108", 9),
    ("Itapipoca", "-3.501042", "-39.579436", 8),
    ("São Gonçalo do Amarante", "-3.611728", "-38.968150", 9),
    ("Tururu", "-3.599536", "-39.435876", 10),
    ("Umirim", "-3.681740", "-39.347648", 10),
    ("Uruburetama", "-3.623077", "-39.514236", 10),
    ("Apuiarés", "-3.947945", "-39.431991", 11),
    ("Pentecoste", "-3.792128", "-39.269460", 11),
    ("São Luís do Curu", "-3.669015", "-39.446448", 11),
    ("Tejuçuoca", "-3.988974", "-39.581174", 11),
    ("Canindé","-4.355676","-39.311455", 12),
    ("Caridade","-4.225344","-39.205636", 12),
    ("Itatira", "-4.526875", "-39.731862", 12),
    ("Paramoti", "-4.099643", "-39.241976", 12),
    ("Acarape", "-4.223809", "-38.707631", 13),
    ("Aracoiaba", "-4.373520", "-38.810717", 13),
    ("Aratuba", "-4.411286", "-39.049615", 13),
    ("Baturité", "-4.326222", "-38.885853", 13),
    ("Capistrano", "-4.462357", "-38.904283", 13),
    ("General Sampaio", "-4.042157", "-39.455592", 11),
    ("itapajé", "-3.686576", "-39.585581", 10),
    ("Redenção", "-4,224384", "-38,729084", 13),
    ("Guaramiranga", "-4,261799", "-38,933177", 13),
    ("Mulungu", "-4,301157", "-38,992017", 13),
    ("Pacoti", "-4,225243", "-38,921261", 13),
    ("Barreira", "-4,287041", "-38,640427", 14),
    ("Chorozinho", "-4,310965", "-38,498658", 14),
    ("Ocara", "-4,491435", "-38,593894", 14),
    ("Beberibe", "-4,186602", "-38,126427", 15),
    ("Cascavel", "-4,133258", "-38,242955", 15),
    ("Pindoretama", "-4,0207", "-38,292837", 15)
);
    

