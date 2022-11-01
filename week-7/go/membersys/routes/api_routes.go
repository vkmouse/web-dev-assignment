package routes

import (
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

func (r *Router) memberGet(ctx *gin.Context) {
	username, success := ctx.GetQuery("username")
	session := sessions.Default(ctx)
	isValid := success && session.Get("name") != nil
	if isValid {
		r.memberGetIfValid(ctx, username)
		return
	}
	ctx.JSON(200, gin.H{"data": nil})
}

func (r *Router) memberGetIfValid(ctx *gin.Context, username string) {
	member := r.unitOfWork.MemberRepository.GetMemberByUsername(username)
	success := member.Id != -1
	if success {
		ctx.JSON(200, gin.H{
			"data": gin.H{
				"id":       member.Id,
				"name":     member.Name,
				"username": member.Username,
			},
		})
		return
	}
	ctx.JSON(200, gin.H{"data": nil})
}

func (r *Router) memberPatch(ctx *gin.Context) {
	if ctx.ContentType() == "application/json" {
		session := sessions.Default(ctx)
		id := session.Get("id")
		var nameRequestBody struct{ Name string }
		ctx.BindJSON(&nameRequestBody)
		if nameRequestBody.Name != "" && id != nil {
			r.memberPatchIfValid(ctx, id.(int), nameRequestBody.Name)
			return
		}
	}

	ctx.JSON(200, gin.H{"error": true})
}

func (r *Router) memberPatchIfValid(ctx *gin.Context, id int, newName string) {
	success := r.unitOfWork.MemberRepository.UpdateNameById(id, newName)
	if success {
		ctx.JSON(200, gin.H{"ok": true})
	} else {
		ctx.JSON(200, gin.H{"error": true})
	}
}
