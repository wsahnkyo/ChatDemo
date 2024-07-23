from modelscope import AutoModelForCausalLM, AutoTokenizer, GenerationConfig


class ChatModel:
    def __init__(self):
        model_path = r"E:\model\Qwen-1_8B-Chat"
        # Note: The default behavior now has injection attack prevention off.
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, revision='master', trust_remote_code=True)
        # use auto mode, automatically select precision based on the device.
        self.model = AutoModelForCausalLM.from_pretrained(model_path, revision='master', device_map="cuda:0",
                                                     trust_remote_code=True).eval()

    def getResult(self, prompt,history):
        # 第一轮对话 1st dialogue turn
        response, history = self.model.chat(self.tokenizer, prompt, history=history)
        return response,history
        # 你好！很高兴为你提供帮助。
        #
        # # 第二轮对话 2nd dialogue turn
        # response, history = self.model.chat(self.tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。",
        #                                      history=history)
        # print(response)
        # # 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
        # # 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
        # # 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
        # # 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
        # # 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
        # # 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。
        #
        # # 第三轮对话 3rd dialogue turn
        # response, history = self.model.chat(self.tokenizer, "给这个故事起一个标题", history=history)
        # print(response)
        # # 《奋斗创业：一个年轻人的成功之路》
        #
        # # Qwen-1.8B-Chat现在可以通过调整系统指令（System Prompt），实现角色扮演，语言风格迁移，任务设定，行为设定等能力。
        # # Qwen-1.8B-Chat can realize roly playing, language style transfer, task setting, and behavior setting by system prompt.
        # response, _ = self.model.chat(self.tokenizer, "你好呀", history=None, system="请用二次元可爱语气和我说话")
        # print(response)
        # # 你好啊！我是一只可爱的二次元猫咪哦，不知道你有什么问题需要我帮忙解答吗？
        #
        # response, _ = self.model.chat(self.tokenizer, "My colleague works diligently", history=None,
        #                                system="You will write beautiful compliments according to needs")
        # print(response)
        # Your colleague is an outstanding worker! Their dedication and hard work are truly inspiring. They always go above and beyond to ensure that
        # their tasks are completed on time and to the highest standard. I am lucky to have them as a colleague, and I know I can count on them to handle any challenge that comes their way.
