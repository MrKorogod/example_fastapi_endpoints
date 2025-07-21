






class SomeLoader:

    @classmethod
    async def get_all(cls, filter_params: SomeFilterParams, transport: AppTransport) -> List[SomeResponseDto]:
        return [SomeResponseDto(id=1, name="test"), SomeResponseDto(id=2, name="test2")]

    @classmethod
    async def get(cls, organization_id:int, transport: AppTransport) -> SomeResponseDto:
        return SomeResponseDto(id=organization_id, name="test")

    @classmethod
    async def create(cls, in_dto: SomeDto.Create, transport: AppTransport) -> SomeResponseDto:
        return SomeResponseDto(id=1, name=in_dto.name)

    @classmethod
    async def update(cls, organization_id:int, in_dto: SomeDto.Update, transport: AppTransport)-> SomeResponseDto:
        return SomeResponseDto(id=organization_id, name=in_dto.name)

    @classmethod
    async def transfer_to_archive(cls, organization_id:int, transport: AppTransport)-> SomeResponseDto:
        return SomeResponseDto(id=organization_id, name="test")