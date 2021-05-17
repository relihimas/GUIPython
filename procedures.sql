ALTER PROCEDURE [dbo].[prcd_checagemEmail]
	@varUsuario nvarchar(20),
	@varSenha	nvarchar(20)
AS
BEGIN
DECLARE cursor_checkemail CURSOR FOR
	SELECT idPermissao FROM userLogin
	WHERE nmUsuario = @varUsuario
	AND	snUsuario = @varSenha
	OPEN cursor_checkemail
	FETCH FROM cursor_checkemail
CLOSE cursor_checkemail;
DEALLOCATE cursor_checkemail;
END;

##########################################################################################################################################################

ALTER PROCEDURE [dbo].[prcd_cadastrousuario]
    @varNome        nvarchar(100),
    @varEndereco    nvarchar(300),
    @varCidade      nvarchar(200),
    @varCompanhia   nvarchar(50),
    @varData        date
AS
BEGIN
    INSERT INTO [Teste].[dbo].[Usuario] VALUES (@varNome, @varEndereco, @varCidade, @varCompanhia, @varData)
END;

##########################################################################################################################################################

CREATE PROCEDURE prcd_insertUser
	@varUser nvarchar(20),
	@varPsswrd nvarchar(20),
	@varKey nvarchar(200)
AS
BEGIN
	INSERT INTO [Teste].[dbo].[userLogin] VALUES (@varUser, @varPsswrd, @varKey)
END;
