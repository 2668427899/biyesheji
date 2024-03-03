const menu = {
    list() {
        return [{"backMenu":[{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-album","buttons":["新增","查看","修改","删除"],"menu":"用户","menuJump":"列表","tableName":"yonghu"}],"menu":"用户管理"},{"child":[{"allButtons":["新增","查看","修改","删除","品牌统计","运行内存","评论数","机身颜色","机身内存","首页总数","首页统计","生成数据","爬取数据"],"appFrontIcon":"cuIcon-similar","buttons":["查看","删除","爬取数据","生成数据"],"menu":"手机","menuJump":"列表","tableName":"shouji"}],"menu":"手机管理"},{"child":[{"allButtons":["查看","修改"],"appFrontIcon":"cuIcon-send","buttons":["查看","修改"],"menu":"系统简介","tableName":"systemintro"}],"menu":"系统管理"}],"frontMenu":[],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","品牌统计","运行内存","评论数","机身颜色","机身内存","首页总数","首页统计","生成数据","爬取数据"],"appFrontIcon":"cuIcon-similar","buttons":["查看"],"menu":"手机","menuJump":"列表","tableName":"shouji"}],"menu":"手机管理"}],"frontMenu":[],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"用户","tableName":"yonghu"}]
    }
}
export default menu;
